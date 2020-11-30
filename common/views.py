from django.core.paginator import Paginator
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.
from articles.models import Article


def index(request):
    template = loader.get_template('common/home.html')
    articles_list = Article.objects.order_by('id').reverse()
    paginator = Paginator(articles_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {"articles_list": articles_list, "page_obj": page_obj}
    return HttpResponse(template.render(context, request))


def categories(request):
    template = loader.get_template('common/categories.html')
    context = {}
    return HttpResponse(template.render(context, request))


def gallery(request):
    template = loader.get_template('common/gallery.html')
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
