from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import Displayable, Ownable, RichText, Slugged
from mezzanine.utils.models import AdminThumbMixin, upload_to
import datetime


class Resource(Displayable, Ownable, RichText, AdminThumbMixin):
    '''Resource content type.
    '''

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

    admin_thumb_field = "featured_image"

    class Meta:
        verbose_name = _("Resource")
        verbose_name_plural = _("Resources")
        ordering = ("title",)

    @models.permalink
    def get_absolute_url(self):
        return ('resource', (), {"slug": self.slug})


class Faq(Displayable, Ownable, RichText, AdminThumbMixin):
    '''FAQ entry content type.
    '''

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

    admin_thumb_field = "featured_image"

    class Meta:
        verbose_name = _("FAQ Entry")
        verbose_name_plural = _("FAQ Entries")
        ordering = ("title",)

    @models.permalink
    def get_absolute_url(self):
        return ('faq', (), {"slug": self.slug})


class Dictionary(Displayable, Ownable, RichText, AdminThumbMixin):
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

    class Meta:
        verbose_name = _("Dictionary Definition")
        verbose_name_plural = _("Dictionary Definitions")
        ordering = ("title",)

    @models.permalink
    def get_absolute_url(self):
        return ('dictionary', (), {"slug": self.slug})


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