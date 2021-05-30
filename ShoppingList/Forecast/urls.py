from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.indexView, name='indexView'),
    path('buy/', views.buyView, name='buy'),
    path('forecast/', views.forecastView, name='forecast')
]