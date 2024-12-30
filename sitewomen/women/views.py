from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'women/index.html', data)

def about(request):
    data = {'title': 'О сайте'}
    return render(request, 'women/about.html', data)

def categories(request, cat_slug):
    return HttpResponse(f'<h1>Страница с категорией {cat_slug}')

def archive(request, year):
    if year > 2025:
        url_redirect = reverse('cats', args=('music',))
        return HttpResponsePermanentRedirect(url_redirect)

    return HttpResponse(f'Страница с архивом {year} года') 

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')