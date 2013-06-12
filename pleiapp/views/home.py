from pleiapp.models import Resource
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def homepage(request, *args, **kwargs):
    resources = Resource.objects.all()
    context = RequestContext(request, locals())
    return render_to_response('index.html', locals(), context_instance=context)