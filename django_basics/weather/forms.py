from .models import WeatherData

from django.forms import ModelForm, TextInput, DateTimeInput, NumberInput


class WeatherDataForm(ModelForm):
    class Meta:
        model = WeatherData
        fields = ["country", "city", "weather", "description", "temperature", "feels_like", "wind_speed"]

        widgets = {
            "country": TextInput(attrs={"class": "form-control", "placeholder": "Country"}),
            "city": TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            "weather": TextInput(attrs={'class': 'form-control', 'placeholder': 'Weather'}),
            "description": TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            "temperature": NumberInput(attrs={'class': 'form-control', 'placeholder': 'Temperature'}),
            "feels_like": NumberInput(attrs={'class': 'form-control', 'placeholder': 'Feels like'}),
            "wind_speed": NumberInput(attrs={'class': 'form-control', 'placeholder': 'Wind speed'}),
            "created_at": DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
        }
