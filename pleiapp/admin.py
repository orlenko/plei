from django.contrib import admin
from mezzanine.pages.admin import PageAdmin

from .models import ContentTypeResource

admin.site.register(ContentTypeResource, PageAdmin)