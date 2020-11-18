from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=60)
    image = models.TextField(default="")
    articles = models.TextField(default="")
    info = models.TextField(default="")
    email = models.EmailField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, default="Anonymous", on_delete=models.SET_DEFAULT)
    text = models.TextField(default="")
    create_date = models.TextField(default="")
    last_modified = models.TextField(default="")
    image = models.TextField(default="")
    summary = models.TextField(default="")
    page_views = models.IntegerField(default=0)
    comments = models.TextField(default="")

    def __str__(self):
        return self.title
