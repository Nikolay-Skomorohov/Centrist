from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader
from articles.models import Article


def article_page(request, article_id):
    template = loader.get_template('articles/article_page.html')
    context = {"current_article": get_object_or_404(Article, pk=article_id)}
    return HttpResponse(template.render(context, request))
