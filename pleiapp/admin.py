from django.contrib import admin
from mezzanine.pages.admin import PageAdmin

from .models import Type, Category, Topic, Resource

admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Resource, PageAdmin)