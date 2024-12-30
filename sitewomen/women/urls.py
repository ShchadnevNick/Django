from tkinter.font import names
from django.urls import path, register_converter
from women.views import index, about

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),

]