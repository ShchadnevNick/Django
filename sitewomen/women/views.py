from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.shortcuts import redirect
from django.urls import reverse

def index(request):
    return HttpResponse('<h1>Главная страница!</h1>')

def about(request):
    return HttpResponse('<h1>О сайте</h1>')

def categories(request, cat_slug):
    return HttpResponse(f'<h1>Страница с категорией {cat_slug}')

def archive(request, year):
    if year > 2025:
        url_redirect = reverse('cats', args=('music',))
        return HttpResponsePermanentRedirect(url_redirect)

    return HttpResponse(f'Страница с архивом {year} года') 

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')