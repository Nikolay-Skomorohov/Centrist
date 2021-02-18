from django.shortcuts import render, get_object_or_404
from articles.models import Article


def article_page(request, article_id):
    context = {"current_article": get_object_or_404(Article, pk=article_id)}
    return render(request, "articles/article_page.html", context)
