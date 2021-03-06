from copy import deepcopy

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.core.admin import DisplayableAdmin, OwnableAdmin
from pleiapp.models import (FrontPageItem,
                            Type,
                            Category,
                            Topic,
                            Resource,
                            Faq,
                            Dictionary,
                            Tagline)


resource_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
resource_fieldsets[0][1]["fields"].insert(1, "categories")
resource_fieldsets[0][1]["fields"].insert(1, "types")
resource_fieldsets[0][1]["fields"].insert(1, "topics")
resource_fieldsets[0][1]["fields"].insert(1, "author")
resource_fieldsets[0][1]["fields"].extend(["content", ])
resource_fieldsets[0][1]["fields"].extend(["toc","video_url","audio_file","link_url","attached_document",])
resource_list_display = ["title", "user", "status", "admin_link"]
resource_fieldsets[0][1]["fields"].insert(-2, "featured_image")
resource_list_display.insert(0, "admin_thumb")
resource_fieldsets = list(resource_fieldsets)
resource_list_filter = deepcopy(DisplayableAdmin.list_filter) + ("categories", "types", "topics", )
resource_fieldsets.insert(1, (_("Related"), {
    "classes": ("collapse-closed",),
    "fields": ("detect_automatically", "related_resources","related_faqs","related_dictionary","searchable_text")}))


class ResourceAdmin(DisplayableAdmin, OwnableAdmin):
    fieldsets = resource_fieldsets
    list_display = resource_list_display
    list_filter = resource_list_filter
    filter_horizontal = ("categories", "types", "topics", "related_resources", "related_dictionary", "related_faqs")
    readonly_fields = ('searchable_text',)

    class Media:
        css = {
             'all': ('/static/css/admin.css',)
        }

    def save_form(self, request, form, change):
        """
        Super class ordering is important here - user must get saved first.
        """
        OwnableAdmin.save_form(self, request, form, change)
        return DisplayableAdmin.save_form(self, request, form, change)

    def save_related(self, request, form, formsets, change):
        retval = super(ResourceAdmin, self).save_related(request, form, formsets, change)
        if form.instance.detect_automatically:
            form.instance.detect_automatically = False
            form.instance.save()
            form.instance.detect_related()
        return retval


faq_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
faq_fieldsets[0][1]["fields"].insert(1, "categories")
faq_fieldsets[0][1]["fields"].insert(1, "types")
faq_fieldsets[0][1]["fields"].insert(1, "topics")
faq_fieldsets[0][1]["fields"].extend(["question_details", "content", ])
faq_fieldsets[0][1]["fields"].insert(-2, "featured_image")
faq_fieldsets = list(faq_fieldsets)
faq_fieldsets.insert(1, (_("Related"), {
    "classes": ("collapse-closed",),
    "fields": ("detect_automatically", "related_resources","related_faqs","related_dictionary","searchable_text",)}))


class FaqAdmin(DisplayableAdmin, OwnableAdmin):
    fieldsets = faq_fieldsets
    list_display = resource_list_display
    list_filter = resource_list_filter
    filter_horizontal = ("categories", "types", "topics", "related_resources","related_faqs","related_dictionary")
    readonly_fields = ('searchable_text',)

    def save_form(self, request, form, change):
        """
        Super class ordering is important here - user must get saved first.
        """
        OwnableAdmin.save_form(self, request, form, change)
        return DisplayableAdmin.save_form(self, request, form, change)

    def save_related(self, request, form, formsets, change):
        retval = super(FaqAdmin, self).save_related(request, form, formsets, change)
        if form.instance.detect_automatically:
            form.instance.detect_automatically = False
            form.instance.save()
            form.instance.detect_related()
        return retval


dictionary_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
dictionary_fieldsets[0][1]["fields"].extend(["content", ])
dictionary_fieldsets[0][1]["fields"].insert(-2, "featured_image")
dictionary_fieldsets = list(dictionary_fieldsets)
dictionary_fieldsets.insert(1, (_("Related"), {
    "classes": ("collapse-closed",),
    "fields": ("related_resources","related_faqs","related_dictionary","searchable_text",)}))


class DictionaryAdmin(DisplayableAdmin, OwnableAdmin):
    fieldsets = dictionary_fieldsets
    list_display = resource_list_display
    list_filter = deepcopy(DisplayableAdmin.list_filter)
    filter_horizontal = ("related_resources","related_faqs","related_dictionary")
    readonly_fields = ('searchable_text',)

    def save_form(self, request, form, change):
        """
        Super class ordering is important here - user must get saved first.
        """
        OwnableAdmin.save_form(self, request, form, change)
        return DisplayableAdmin.save_form(self, request, form, change)


class CategoryAdmin(admin.ModelAdmin):
    list_display =['__str__', 'visible']
    list_filter = ['visible',]


class TypeAdmin(admin.ModelAdmin):
    list_display =['__str__', 'visible']
    list_filter = ['visible',]


class TopicAdmin(admin.ModelAdmin):
    list_display =['__str__', 'visible']
    list_filter = ['visible',]


class FrontPageItemAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'admin_thumb', 'visible']
    list_filter = ['visible',]


admin.site.register(Resource, ResourceAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Dictionary, DictionaryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(FrontPageItem, FrontPageItemAdmin)
admin.site.register(Tagline, admin.ModelAdmin)
