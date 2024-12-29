from django.urls import path, re_path, register_converter

from women.converters import FourDigitYeadConverter
from women.views import index, about, categories, archive

register_converter(FourDigitYeadConverter, 'year4')


urlpatterns = [
    path('', index),
    path('about/', about),
    path('cats/<slug:cat_slug>/', categories),
    path('archive/<year4:year>/', archive)  
]