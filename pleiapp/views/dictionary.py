from pleiapp import models
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
import string


def full_list(request):
    index = string.uppercase
    tops = []
    for letter in index:
        tops.append((letter, models.Dictionary.objects.filter(title__istartswith=letter)[:5]))
    context = RequestContext(request, locals())
    return render_to_response('dictionary/full_list.html', locals(), context_instance=context)


def dictionary_letter(request, letter):
    records = models.Dictionary.objects.filter(title__istartswith=letter)
    context = RequestContext(request, locals())
    return render_to_response('dictionary/letter_list.html', locals(), context_instance=context)