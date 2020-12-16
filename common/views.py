from django.core.paginator import Paginator
from django.shortcuts import render
from articles.models import Article


def home(request):
    articles_list = Article.objects.order_by('id').reverse()
    paginator = Paginator(articles_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "articles_list": articles_list,
        "page_obj": page_obj,
    }

    return render(request, 'common/home.html', context)


def categories(request):
    context = {}

    return render(request, 'common/categories.html', context)


def gallery(request):
    context = {}

    return render(request, 'common/gallery.html', context)


def about(request):
    context = {}

    return render(request, 'common/about.html', context)


def profile(request):
    context = {}

    return render(request, 'common/profile.html', context)
