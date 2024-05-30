from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

from .forms import WeatherDataForm
from .models import WeatherData

# Create your views here.


class WeatherDetailView(DetailView):
    model = WeatherData
    template_name = 'weather/weather_detail.html'
    context_object_name = 'weather_note'


class WeatherUpdateView(UpdateView):
    model = WeatherData
    template_name = 'weather/create.html'

    form_class = WeatherDataForm


class WeatherDeleteView(DeleteView):
    model = WeatherData
    success_url = '/weather'
    template_name = 'weather/weather_delete.html'


def weather_home(request):
    weather_data = WeatherData.objects.order_by('-created_at')[:3]
    return render(request, 'weather/weather_home.html', {'weather_data': weather_data})


def create(request):
    error: str = ''
    if request.method == 'POST':
        form = WeatherDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('weather_home')
        else:
            error = 'Something went wrong'

    form = WeatherDataForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'weather/create.html', data)

