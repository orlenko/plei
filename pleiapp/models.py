from django.utils.translation import ugettext_lazy as _
from django.db import models
from mezzanine.core.models import Ownable
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText


class Named(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    class Meta:
        abstract = True

    def __unicode__(self):
        return  '%s: "%s"' % (type(self).__name__, self.name)

class Topic(Named):
    '''Topics for resources.
    '''


class Type(Named):
    '''Types for resources.
    '''


class Category(Named):
    '''Categories for resources.
    '''

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Resource(Page, RichText, Ownable):
    '''Resource content type.
    '''
    types = models.ManyToManyField(Type)
    topics = models.ManyToManyField(Topic)
    categories = models.ManyToManyField(Category)

