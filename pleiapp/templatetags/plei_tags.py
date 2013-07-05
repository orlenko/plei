
from django.template import Context, TemplateSyntaxError, Variable
from django.template.loader import get_template

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


@register.render_tag
def plei_top_menu(context, token):
    topics = models.Topic.objects.filter(visible=True)
    categories = models.Category.objects.filter(visible=True)
    types = models.Type.objects.filter(visible=True)
    context["topics"] = topics
    context["categories"] = categories
    context["types"] = types
    t = get_template('plei/top_menu.html')
    return t.render(Context(context))


@register.render_tag
def plei_side_menu(context, token):
    topics = models.Topic.objects.filter(visible=True)
    categories = models.Category.objects.filter(visible=True)
    types = models.Type.objects.filter(visible=True)
    context["topics"] = topics
    context["categories"] = categories
    context["types"] = types
    t = get_template('plei/side_menu.html')
    return t.render(Context(context))


@register.render_tag
def plei_taglines(context, token):
    context['taglines'] = models.Tagline.objects.all()
    t = get_template('plei/taglines.html')
    return t.render(Context(context))