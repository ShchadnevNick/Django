from django.http import HttpResponse, HttpResponseNotFound, Http404

def index(request):
    return HttpResponse('<h1>Главная страница!</h1>')

def about(request):
    return HttpResponse('<h1>О сайте</h1>')

def categories(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Страница с категорией {cat_slug}')

def archive(request, year):
    if year > 2025:
        raise Http404

    return HttpResponse(f'Страница с архивом {year} года')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')