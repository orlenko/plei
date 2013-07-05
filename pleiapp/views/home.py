from django.shortcuts import render_to_response
from django.template.context import RequestContext
from pleiapp import models


def homepage(request, *args, **kwargs):
    front_page_items = models.FrontPageItem.objects.filter(visible=True).order_by('-pub_date')
    context = RequestContext(request, locals())
    return render_to_response('index.html', {}, context_instance=context)