from django.urls import path

from . import views

urlpatterns = [
    path('', views.weather_home, name='weather_home'),
    # path('about/', views.about, name='about'),
]
