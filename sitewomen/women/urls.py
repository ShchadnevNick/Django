from django.urls import path
from women.views import index, about

urlpatterns = [
    path('', index),
    path('about/', about),
]