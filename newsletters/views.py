from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def newsletter(request):
    template = loader.get_template('newsletters/newsletter.html')
    context = {}
    return HttpResponse(template.render(context, request))
