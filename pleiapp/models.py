from django.utils.translation import ugettext_lazy as _
from django.db import models
from mezzanine.core.models import Ownable
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText


class Topic(models.Model):
    '''Topics for resources.
    '''
    name = models.CharField(_('Name'), max_length=255)


class Type(models.Model):
    '''Types for resources.
    '''
    name = models.CharField(_('Name'), max_length=255)


class Category(models.Model):
    '''Categories for resources.
    '''
    name = models.CharField(_('Name'), max_length=255)


class ContentTypeResource(Page, RichText, Ownable):
    '''Resource content type.

    Inherited fields:

    > from Ownable:
        user = FK(user)

    > from Sluggable
        title = CharField
        slug  = CharField

    > from MetaData:
        _meta_title = CharField
        description = TextField
        gen_description = BooleanField
        keywords = KeywordsField

    > from Orderable
        _order = IntegerField

    > from Displayable
        status = IntegerField
        publish_date = DateTimeField
        expiry_date = DateTimeField
        short_url = URLField
        in_sitemap = BooleanField

    > from Page
        parent = FK(Page)
        in_menus = MenusField
        titles = CharField
        content_model = CharField
        login_required = BooleanField

    > from RichText
        content = RichTextField()

    '''

    class Meta:
        verbose_name = _("Resource")
        verbose_name_plural = _("Resources")

    types = models.ManyToManyField(Type)
    topics = models.ManyToManyField(Topic)
    categories = models.ManyToManyField(Category)

