from tkinter.font import names

from django.urls import path, register_converter

from women.converters import FourDigitYeadConverter
from women.views import index, about, categories, archive

register_converter(FourDigitYeadConverter, 'year4')

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('cats/<slug:cat_slug>/', categories, name='cats'),
    path('archive/<year4:year>/', archive, name='archive'),
]