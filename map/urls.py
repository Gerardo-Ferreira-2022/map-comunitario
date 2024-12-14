from django.urls import path
from .views import index, menu


urlpatterns = [
    path('', index, name='home'),
    path('menu/', menu, name='menu'),
]