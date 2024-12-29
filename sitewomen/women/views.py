from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('<h1>Главная страница!</h1>')

def about(request):
    return HttpResponse('<h1>О сайте</h1>')

