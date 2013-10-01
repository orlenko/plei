
from django.conf.urls import patterns, include, url
from django.contrib import admin
import logging


log = logging.getLogger('pleiapp.urls')




admin.autodiscover()


def group_url(group):
    retval = url('^%s/(?P<slug>.*)/$' % group,
                 'pleiapp.views.groups.%s' % group,
                 {},
                 name=group)
    log.debug('Adding URL: %s' % retval)
    return retval


def content_url(typename):
    retval = url('^%s/(?P<slug>.*)/$' % typename,
               'pleiapp.views.content_types.%s' % typename,
               {},
               name=typename)
    log.debug('Adding URL: %s' % retval)
    return retval


urlpatterns = patterns("",

    # Change the admin prefix here to use an alternate URL for the
    # admin interface, which would be marginally more secure.
    ("^admin/", include(admin.site.urls)),
    url("^$", "pleiapp.views.home.homepage", {}, name="home"),

    url('^dictionary/$', 'pleiapp.views.dictionary.full_list', {}, name='dictionary-full'),
    url('^dictionary/(?P<letter>.)/$', 'pleiapp.views.dictionary.dictionary_letter', {}, name='dictionary-letter'),

    group_url('category'),
    group_url('resource_type'),
    group_url('topic'),
    content_url('resource'),
    content_url('faq'),
    content_url('dictionary'),
	
    ("^captcha/", include('captcha.urls')), # Slap it in before the catch-all ("^", include("mezzanine.urls")),

    ("^", include("mezzanine.urls")),
)

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
