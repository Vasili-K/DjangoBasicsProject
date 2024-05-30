from django.db import models


class WeatherData(models.Model):
    country = models.CharField('Country', max_length=150)
    city = models.CharField('City', max_length=150)
    weather = models.CharField('Weather', max_length=250)
    description = models.TextField('Description')
    temperature = models.FloatField('Temperature')
    feels_like = models.FloatField('Feels like')
    wind_speed = models.FloatField('Wind speed')
    created_at = models.DateTimeField('Date of request', auto_now_add=True)

    def get_absolute_url(self):
        return f'/weather/{self.pk}'

    def __str__(self):
        return f'{self.city}: {self.weather}, {self.temperature} '

    class Meta:
        verbose_name = 'Weather Data'
        verbose_name_plural = 'Weather Data'
