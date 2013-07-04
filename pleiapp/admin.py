from .models import Type, Category, Topic, Resource
from copy import deepcopy

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.core.admin import DisplayableAdmin, OwnableAdmin


resource_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
resource_fieldsets[0][1]["fields"].insert(1, "categories")
resource_fieldsets[0][1]["fields"].insert(1, "types")
resource_fieldsets[0][1]["fields"].insert(1, "topics")
resource_fieldsets[0][1]["fields"].extend(["content", ])
resource_list_display = ["title", "user", "status", "admin_link"]
resource_fieldsets[0][1]["fields"].insert(-2, "featured_image")
resource_list_display.insert(0, "admin_thumb")
resource_fieldsets = list(resource_fieldsets)
resource_fieldsets.insert(1, (_("Other posts"), {
    "classes": ("collapse-closed",),
    "fields": ("related_resources",)}))
resource_list_filter = deepcopy(DisplayableAdmin.list_filter) + ("categories", "types", "topics",)


class ResourceAdmin(DisplayableAdmin, OwnableAdmin):
    fieldsets = resource_fieldsets
    list_display = resource_list_display
    list_filter = resource_list_filter
    filter_horizontal = ("categories", "types", "topics", "related_resources",)

    def save_form(self, request, form, change):
        """
        Super class ordering is important here - user must get saved first.
        """
        OwnableAdmin.save_form(self, request, form, change)
        return DisplayableAdmin.save_form(self, request, form, change)


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": ("title",)}),)

    def in_menu(self):
        for (_name, items) in settings.ADMIN_MENU_ORDER:
            if "pleiapp.ResourceCategory" in items:
                return True
        return False

class TypeAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": ("title",)}),)

    def in_menu(self):
        for (_name, items) in settings.ADMIN_MENU_ORDER:
            if "pleiapp.ResourceCategory" in items:
                return True
        return False

class TopicAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": ("title",)}),)

    def in_menu(self):
        for (_name, items) in settings.ADMIN_MENU_ORDER:
            if "pleiapp.ResourceCategory" in items:
                return True
        return False


admin.site.register(Resource, ResourceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Topic, TopicAdmin)
