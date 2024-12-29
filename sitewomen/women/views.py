from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse('<h1>Главная страница!</h1>')

def about(request):
    return HttpResponse('<h1>О сайте</h1>')

def categories(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Страница с категории {cat_slug}')

def archive(request, year):
    return HttpResponse(f'Страница с архивом {year} года')
