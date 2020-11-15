from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.
from articles.models import Article


def index(request):
    template = loader.get_template('common/home.html')
    context = {"articles_list": Article.objects.all, }
    return HttpResponse(template.render(context, request))


def categories(request):
    template = loader.get_template('common/categories.html')
    context = {}
    return HttpResponse(template.render(context, request))


def gallery(request):
    template = loader.get_template('common/gallery.html')
    context = {}
    return HttpResponse(template.render(context, request))


def newsletter(request):
    template = loader.get_template('common/newsletter.html')
    context = {}
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('common/about.html')
    context = {}
    return HttpResponse(template.render(context, request))


def profile(request):
    template = loader.get_template('common/profile.html')
    context = {}
    return HttpResponse(template.render(context, request))
