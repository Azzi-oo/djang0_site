from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse


def index(request):
    return HttpResponse("Страница приложения women")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьм по категориям</h><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статьм по категориям</h><p>slug: {cat_slug}</p>")


def archieve(request, year):
    if year > 2023:
        url = reverse('cats', args={'music', })
        return redirect(url)
    return HttpResponse(f"<h1>Архив по годам: </h><p>year: {year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Cтраница не найдена</h1>")
