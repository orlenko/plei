
from collections import defaultdict

from django.core.exceptions import ImproperlyConfigured
from django.template import Context, TemplateSyntaxError, Variable
from django.template.loader import get_template
from django.utils.translation import ugettext_lazy as _

from mezzanine.pages.models import Page
from mezzanine.utils.urls import admin_url, home_slug
from mezzanine import template

from pleiapp import models


register = template.Library()


@register.render_tag
def plei_tag_menu(context, token):
    model_name = None
    parts = token.split_contents()[1:]
    for part in parts:
        part = Variable(part).resolve(context)
        if isinstance(part, unicode):
            model_name = part
    if not model_name:
        raise TemplateSyntaxError('Failed to extract model name from %s' % token)
    context["plei_tag_model"] = model_name
    model = getattr(models, model_name)
    context["tags"] = model.objects.filter(visible=True).order_by('title')

    t = get_template('plei/tag_menu.html')
    return t.render(Context(context))