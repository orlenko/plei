from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField
from mezzanine.core.models import Displayable, Ownable, RichText, Slugged
from mezzanine.utils.models import AdminThumbMixin, upload_to


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
    featured_image = FileField(verbose_name=_("Featured Image"),
        upload_to=upload_to("blog.BlogPost.featured_image", "blog"),
        format="Image", max_length=255, null=True, blank=True)
    related_resources = models.ManyToManyField("self",
                                 verbose_name=_("Related resources"), blank=True)

    admin_thumb_field = "featured_image"

    class Meta:
        verbose_name = _("Resource")
        verbose_name_plural = _("Resources")
        ordering = ("title",)

    @models.permalink
    def get_absolute_url(self):
        return ('resource', (), {"slug": self.slug})


class Category(Slugged):
    visible = models.NullBooleanField(null=True, default=False)

    class Meta:
        verbose_name = _("Resource Category")
        verbose_name_plural = _("Resource Categories")
        ordering = ("title",)

    @models.permalink
    def get_absolute_url(self):
        return ("resource_category", (), {"category": self.slug})


class Type(Slugged):
    visible = models.NullBooleanField(null=True, default=False)

    class Meta:
        verbose_name = _("Resource Type")
        verbose_name_plural = _("Resource Types")
        ordering = ("title",)

    @models.permalink
    def get_absolute_url(self):
        return ("resource_type", (), {"type": self.slug})


class Topic(Slugged):

    visible = models.NullBooleanField(null=True, default=False)

    class Meta:
        verbose_name = _("Resource Topic")
        verbose_name_plural = _("Resource Topics")
        ordering = ("title",)

    @models.permalink
    def get_absolute_url(self):
        return ("resource_topic", (), {"topic": self.slug})
