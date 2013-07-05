from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField
from mezzanine.core.models import Displayable, Ownable, RichText, Slugged
from mezzanine.utils.models import AdminThumbMixin, upload_to
import datetime


class Resource(Displayable, Ownable, RichText, AdminThumbMixin):
    '''Resource content type.
    '''

    categories = models.ManyToManyField("Category",
                                        verbose_name=_("Categories"),
                                        blank=True, related_name="resources")
    topics = models.ManyToManyField("Topic",
                                    verbose_name=_("Topics"),
                                    blank=True, related_name="resources")
    types = models.ManyToManyField("Type",
                                   verbose_name=_("Types"),
                                   blank=True, related_name="resources")
    author = models.CharField(max_length=1024, blank=True, default='')
    featured_image = FileField(verbose_name=_("Featured Image"),
        upload_to=upload_to("blog.BlogPost.featured_image", "blog"),
        format="Image", max_length=255, null=True, blank=True)
    related_resources = models.ManyToManyField("self",
                                 verbose_name=_("Related resources"),
                                 blank=True)
    related_dictionary = models.ManyToManyField("Dictionary",
                                 verbose_name=_("Related Dictionary Definition"),
                                 blank=True)
    related_faqs = models.ManyToManyField("Faq",
                                 verbose_name=_("Related FAQ Entries"),
                                 blank=True)

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
                                        verbose_name=_("Categories"),
                                        blank=True, related_name="faqs")
    topics = models.ManyToManyField("Topic",
                                    verbose_name=_("Topics"),
                                    blank=True, related_name="faqs")
    types = models.ManyToManyField("Type",
                                   verbose_name=_("Types"),
                                   blank=True, related_name="faqs")
    author = models.CharField(max_length=1024, blank=True, default='')
    featured_image = FileField(verbose_name=_("Featured Image"),
        upload_to=upload_to("blog.BlogPost.featured_image", "blog"),
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

    categories = models.ManyToManyField("Category",
                                        verbose_name=_("Categories"),
                                        blank=True, related_name="dicts")
    topics = models.ManyToManyField("Topic",
                                    verbose_name=_("Topics"),
                                    blank=True, related_name="dicts")
    types = models.ManyToManyField("Type",
                                   verbose_name=_("Types"),
                                   blank=True, related_name="dicts")
    author = models.CharField(max_length=1024, blank=True, default='')
    featured_image = FileField(verbose_name=_("Featured Image"),
        upload_to=upload_to("blog.BlogPost.featured_image", "blog"),
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
    ('page', 'Page'),
    ('dictionary', 'Dictionary Definition'),
    ('calendar', 'Calendar Event'),
    ('resource', 'Resource'),
    ('faq', 'FAQ Entry'),
    ('link', 'External Link'),
)

class FrontPageItem(models.Model, AdminThumbMixin):
    item_type = models.CharField(max_length=255, choices=FRONT_PAGE_ITEM_TYPES)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    title = models.CharField(max_length=255)
    text = models.TextField()
    url = models.URLField()
    order = models.IntegerField(default=0)
    featured_image = FileField(verbose_name=_("Featured Image"),
        upload_to=upload_to("blog.BlogPost.featured_image", "blog"),
        format="Image", max_length=255, null=True, blank=True)
    admin_thumb_field = "featured_image"
    visible = models.NullBooleanField(null=True, default=True)


class Category(Slugged):
    visible = models.NullBooleanField(null=True, default=True)

    class Meta:
        verbose_name = _("Resource Category")
        verbose_name_plural = _("Resource Categories")
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