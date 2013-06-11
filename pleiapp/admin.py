from django.contrib import admin
from mezzanine.pages.admin import PageAdmin

from .models import Resource

admin.site.register(Resource, PageAdmin)