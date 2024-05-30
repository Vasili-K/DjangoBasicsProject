from django.urls import path

from . import views

urlpatterns = [
    path('', views.weather_home, name='weather_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.WeatherDetailView.as_view(), name='weather-detail'),
    path('<int:pk>/update', views.WeatherUpdateView.as_view(), name='weather-update'),
    path('<int:pk>/delete', views.WeatherDeleteView.as_view(), name='weather-delete'),
]
