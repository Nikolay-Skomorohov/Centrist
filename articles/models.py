from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=60, null=False, unique=True)
    image = models.URLField(null=True)
    articles = models.TextField(default="")
    info = models.TextField(default="")
    email = models.EmailField(null=True, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=150, null=False, unique=True)
    author = models.ForeignKey(Author, default="Anonymous", on_delete=models.SET_DEFAULT)
    text = models.TextField(default="")
    create_date = models.TextField(default="")
    last_modified = models.TextField(default="")
    image = models.URLField(null=False)
    summary = models.TextField(default="", max_length=300)
    page_views = models.IntegerField(default=0)
    comments = models.TextField(default="")

    def __str__(self):
        return self.title
