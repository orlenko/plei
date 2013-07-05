from pleiapp import models
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext


def category(request, slug):
    group = get_object_or_404(models.Category, slug=slug)
    context = RequestContext(request, locals())
    return render_to_response('groups/category.html', locals(), context_instance=context)


def resource_type(request, slug):
    group = get_object_or_404(models.Type, slug=slug)
    context = RequestContext(request, locals())
    return render_to_response('groups/restype.html', locals(), context_instance=context)


def topic(request, slug):
    group = get_object_or_404(models.Topic, slug=slug)
    context = RequestContext(request, locals())
    return render_to_response('groups/topic.html', locals(), context_instance=context)
