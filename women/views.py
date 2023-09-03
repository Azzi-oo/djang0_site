from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Страница приложения women")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьм по категориям</h><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статьм по категориям</h><p>slug: {cat_slug}</p>")


def archieve(request, year):
    return HttpResponse(f"<h1>Архив по годам: </h><p>year: {year}</p>")