from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from pleiapp import models


def resource(request, slug):
    page = get_object_or_404(models.Resource, slug=slug)
    return render_to_response('pages/content_type.html', {},
                              context_instance=RequestContext(request, locals()))


def faq(request, slug):
    page = get_object_or_404(models.Faq, slug=slug)
    return render_to_response('pages/content_type.html', {},
                              context_instance=RequestContext(request, locals()))


def dictionary(request, slug):
    page = get_object_or_404(models.Dictionary, slug=slug)
    return render_to_response('pages/content_type.html', {},
                              context_instance=RequestContext(request, locals()))

