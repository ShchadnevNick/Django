from django.http import HttpResponse
from django.shortcuts import render


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

