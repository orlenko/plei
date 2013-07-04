
from django.conf.urls import patterns, include, url
from django.contrib import admin
from mezzanine.conf import settings


admin.autodiscover()

# Leading and trailing slahes for urlpatterns based on setup.
_slashes = (
    "/" if settings.BLOG_SLUG else "",
    "/" if settings.APPEND_SLASH else "",
)

urlpatterns = patterns("",

    # Change the admin prefix here to use an alternate URL for the
    # admin interface, which would be marginally more secure.
    ("^admin/", include(admin.site.urls)),
    url("^$", "pleiapp.views.home.homepage", {}, name="home"),
    url("^%sresource/category/(?P<category>.*)%s$" % _slashes,
        "pleiapp.views.resource.resource_list", name="resource_category"),
    url("^%sresource/type/(?P<type>.*)%s$" % _slashes,
        "pleiapp.views.resource.resource_list", name="resource_type"),
    url("^%sresource/topic/(?P<topic>.*)%s$" % _slashes,
        "pleiapp.views.resource.resource_list", name="resource_topic"),
    url("^%sresource/(?P<slug>.*)%s$" % _slashes,
        "pleiapp.views.resource.resource", {}, name="resource"),


    ("^", include("mezzanine.urls")),
)

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
