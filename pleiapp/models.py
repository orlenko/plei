from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import Displayable, Ownable, RichText, Slugged
from mezzanine.utils.models import AdminThumbMixin, upload_to
import datetime
import string
from django.utils.html import strip_tags
import logging

log = logging.getLogger(__name__)


STOPWORDS = ['all', 'just', 'being', 'over', 'both', 'through', 'yourselves',
             'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under',
             'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during',
             'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further',
             'where', 'few', 'because', 'doing', 'some', 'are', 'our',
             'ourselves', 'out', 'what', 'for', 'while', 'does', 'above',
             'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by',
             'on', 'about', 'of', 'against', 's', 'or', 'own', 'into',
             'yourself', 'down', 'your', 'from', 'her', 'their', 'there',
             'been', 'whom', 'too', 'themselves', 'was', 'until', 'more',
             'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he',
             'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs',
             'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself',
             'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same',
             'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a',
             'off', 'i', 'yours', 'so', 'the', 'having', 'once', 'im', 'its',
             ]


class RelatedMixin(object):
    @property
    def has_related(self):
        return self.related_resources.count() or self.related_faqs.count()

    def update_searchable_text(self):
        self.searchable_text = ' '.join([
            clean_text(self.title),
            clean_text(strip_tags(self.content)),
            clean_text(strip_tags(getattr(self, 'toc', '')))])
        log.debug('Updated searchable text for %s: %s' % (self, self.searchable_text))



class Resource(Displayable, Ownable, RichText, AdminThumbMixin, RelatedMixin):
    '''Resource content type.
    '''

    item_type = 'Resource'

    categories = models.ManyToManyField("Category",
                                        verbose_name=_("Personas"),
                                        blank=True, related_name="resources",
        help_text='Personas applicable to this resource')
    topics = models.ManyToManyField("Topic",
                                    verbose_name=_("Topics"),
                                    blank=True, related_name="resources",
        help_text='Topics related to this resource')
    types = models.ManyToManyField("Type",
                                   verbose_name=_("Types"),
                                   blank=True, related_name="resources",
        help_text='Resource types applicable to this resource')
    author = models.CharField(max_length=1024, blank=True, default='',
        help_text='Name of the person (or names of the people) who created this resource')
    featured_image = FileField(verbose_name=_("Featured Image"),
        upload_to=upload_to("pleiapp.Resource.featured_image", "images"),
        format="Image", max_length=255, null=True, blank=True,
        help_text='The image that will appear with this resource on the category pages')
    related_resources = models.ManyToManyField("self",
                                 verbose_name=_("Related resources"),
                                 blank=True,
                                 help_text='Other resources related to this one')
    related_dictionary = models.ManyToManyField("Dictionary",
                                 verbose_name=_("Related Dictionary Definition"),
                                 blank=True,
                                 help_text='Dictionary entries related to this resource')
    related_faqs = models.ManyToManyField("Faq",
                                 verbose_name=_("Related FAQ Entries"),
                                 blank=True,
                                 help_text='FAQ entries related to this resource')
    video_url = models.URLField("Video", max_length=1024, blank=True, default='', null=True,
        help_text='Paste a YouTube URL here. '
            'Example: http://www.youtube.com/watch?v=6Bm7DVqJTHo')
    link_url = models.URLField("Web Link", max_length=1024, blank=True, default='', null=True,
        help_text='A link to a web resource. '
            'The address must start with http:// or https://. '
            'For example: http://plei.publiclegaled.bc.ca')
    audio_file = FileField("Audio",
        upload_to=upload_to("pleiapp.Resource.audio_file", "resource/audio"),
        extensions=['.mp3','.mp4','.wav','.aiff','.midi','.m4p'],
        max_length=255,
        null=True,
        blank=True,
        help_text='You can upload an audio file. '
            'Acceptable file types: .mp3, .mp4, .wav, .aiff, .m4p.')
    attached_document = FileField('Downloadable Document',
        upload_to=upload_to("pleiapp.Resource.attachment_file", "resource/document"),
        extensions=['.doc','.pdf','.rtf','.txt','.odf','.docx', '.xls', '.xlsx', '.ppt', '.pptx'],
        max_length=255,
        null=True,
        blank=True,
        help_text='You can upload an office document or a PDF file. '
            'Acceptable file types: .doc, .pdf, .rtf, .txt, .odf, .docx, .xls, .xlsx, .ppt, .pptx.')
    toc = RichTextField('Table of Contents', blank=True, null=True,
        help_text='Paste the Table of Contents here')
    detect_automatically = models.NullBooleanField(default=False, null=True)
    searchable_text = models.TextField(null=True, blank=True)

    admin_thumb_field = "featured_image"

    class Meta:
        verbose_name = _("Resource")
        verbose_name_plural = _("Resources")
        ordering = ("title",)

    @models.permalink
    def get_absolute_url(self):
        return ('resource', (), {"slug": self.slug})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.update_searchable_text()
        return super(Resource, self).save(force_insert, force_update, using, update_fields)

    def detect_related(self):
        log.debug('Detecting related to %s' % self)
        words = self.searchable_text.split()
        log.debug('%s words' % len(words))
        pairs = set()
        for index in range(len(words) - 1):
            pairs.add(' '.join([words[index], words[index+1]]))
        log.debug('%s word pairs' % len(pairs))
        for pair in pairs:
            log.debug('Looking for records containing %r' % pair)
            for faq in Faq.objects.filter(searchable_text__contains=pair):
                log.debug('Related FAQ: %s' % faq)
                self.related_faqs.add(faq)
            for dictionary in Dictionary.objects.filter(searchable_text__contains=pair):
                log.debug('Related Dictionary entry: %s' % dictionary)
                self.related_dictionary.add(dictionary)
            for resource in Resource.objects.filter(searchable_text__contains=pair):
                if resource.pk != self.pk:
                    log.debug('Related Resource: %s' % resource)
                    self.related_resources.add(resource)


class Faq(Displayable, Ownable, RichText, AdminThumbMixin, RelatedMixin):
    '''FAQ entry content type.
    '''

    item_type = 'FAQ'

    categories = models.ManyToManyField("Category",
                                        verbose_name=_("Personas"),
                                        blank=True, related_name="faqs")
    topics = models.ManyToManyField("Topic",
                                    verbose_name=_("Topics"),
                                    blank=True, related_name="faqs")
    types = models.ManyToManyField("Type",
                                   verbose_name=_("Types"),
                                   blank=True, related_name="faqs")
    author = models.CharField(max_length=1024, blank=True, default='')
    featured_image = FileField(verbose_name=_("Featured Image"),
        upload_to=upload_to("pleiapp.Faq.featured_image", "images"),
        format="Image", max_length=255, null=True, blank=True)
    related_faqs = models.ManyToManyField("self",
                                 verbose_name=_("Related FAQ Entries"),
                                 blank=True)
    related_dictionary = models.ManyToManyField("Dictionary",
                                 verbose_name=_("Related Dictionary Definition"),
                                 blank=True)
    related_resources = models.ManyToManyField(Resource,
                                 verbose_name=_("Related Resources"),
                                 blank=True,
                                 through=Resource.related_faqs.through)
    detect_automatically = models.NullBooleanField(default=False, null=True)
    searchable_text = models.TextField(null=True, blank=True)

    admin_thumb_field = "featured_image"

    class Meta:
        verbose_name = _("FAQ Entry")
        verbose_name_plural = _("FAQ Entries")
        ordering = ("title",)

    @models.permalink
    def get_absolute_url(self):
        return ('faq', (), {"slug": self.slug})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.update_searchable_text()
        return super(Faq, self).save(force_insert, force_update, using, update_fields)

    def detect_related(self):
        words = self.searchable_text.split()
        pairs = set()
        for index in range(len(words) - 1):
            pairs.add(' '.join([words[index], words[index+1]]))
        for pair in pairs:
            for faq in Faq.objects.filter(searchable_text__contains=pair):
                if faq.pk != self.pk:
                    self.related_faqs.add(faq)
            for dictionary in Dictionary.objects.filter(searchable_text__contains=pair):
                self.related_dictionary.add(dictionary)
            for resource in Resource.objects.filter(searchable_text__contains=pair):
                self.related_resources.add(resource)


class Dictionary(Displayable, Ownable, RichText, AdminThumbMixin, RelatedMixin):
    '''Dictionary Definition content type.
    '''
    author = models.CharField(max_length=1024, blank=True, default='')
    featured_image = FileField(verbose_name=_("Featured Image"),
        upload_to=upload_to("pleiapp.Dictionary.featured_image", "images"),
        format="Image", max_length=255, null=True, blank=True)
    related_dictionary = models.ManyToManyField("self",
                                 verbose_name=_("Related Dictionary Definition"),
                                 blank=True)
    related_resources = models.ManyToManyField(Resource,
                                 verbose_name=_("Related Resources"),
                                 blank=True,
                                 through=Resource.related_dictionary.through)
    related_faqs = models.ManyToManyField(Faq,
                                 verbose_name=_("Related FAQ Entries"),
                                 blank=True,
                                 through=Faq.related_dictionary.through)
    admin_thumb_field = "featured_image"
    searchable_text = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Dictionary Definition")
        verbose_name_plural = _("Dictionary Definitions")
        ordering = ("title",)

    @models.permalink
    def get_absolute_url(self):
        return ('dictionary', (), {"slug": self.slug})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.update_searchable_text()
        return super(Dictionary, self).save(force_insert, force_update, using, update_fields)


FRONT_PAGE_ITEM_TYPES = (
    ('plei', 'PLEI'),
    ('event', 'Event'),
    ('project', 'Project'),
    ('type', 'Type'),
    ('persona', 'Persona'),
    ('topic', 'Topic'),
    ('pls', 'PLS'),
)


class FrontPageItem(models.Model, AdminThumbMixin):
    item_type = models.CharField(max_length=255, choices=FRONT_PAGE_ITEM_TYPES)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    title = models.CharField(max_length=255)
    text = models.TextField()
    url = models.URLField()
    order = models.IntegerField(default=0)
    featured_image = FileField(verbose_name=_("Featured Image"),
        upload_to=upload_to("pleiapp.FeaturedItem.featured_image", "images"),
        format="Image", max_length=255, null=True, blank=True)
    admin_thumb_field = "featured_image"
    visible = models.NullBooleanField(null=True, default=True)

    def __unicode__(self):
        return self.title


class Category(Slugged):
    visible = models.NullBooleanField(null=True, default=True)

    class Meta:
        verbose_name = _("Persona")
        verbose_name_plural = _("Personas")
        ordering = ("title",)

    @models.permalink
    def get_absolute_url(self):
        return ("category", (), {"slug": self.slug})


class Type(Slugged):
    visible = models.NullBooleanField(null=True, default=True)

    class Meta:
        verbose_name = _("Resource Type")
        verbose_name_plural = _("Resource Types")
        ordering = ("title",)

    @models.permalink
    def get_absolute_url(self):
        return ("resource_type", (), {"slug": self.slug})


class Topic(Slugged):

    visible = models.NullBooleanField(null=True, default=True)

    class Meta:
        verbose_name = _("Resource Topic")
        verbose_name_plural = _("Resource Topics")
        ordering = ("title",)

    @models.permalink
    def get_absolute_url(self):
        return ("topic", (), {"slug": self.slug})


class Tagline(models.Model):
    text = models.TextField()

    def __unicode__(self):
        return self.text


def clean_text(text):
    text = text.encode('utf8').translate(None, string.punctuation)
    return ' '.join([x for x in text.lower().split() if 2 < len(x) and x not in STOPWORDS])