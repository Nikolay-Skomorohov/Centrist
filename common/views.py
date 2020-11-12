from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Test Test Test Test Test")


def test2(request):
    return HttpResponse("Test 2")