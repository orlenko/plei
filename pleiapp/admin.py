from django.contrib import admin
from mezzanine.pages.admin import PageAdmin

from .models import Type, Category, Topic, Resource

admin.site.register(Type, PageAdmin)
admin.site.register(Category, PageAdmin)
admin.site.register(Topic, PageAdmin)
admin.site.register(Resource, PageAdmin)