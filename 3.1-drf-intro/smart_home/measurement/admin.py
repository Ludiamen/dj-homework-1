from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Sensor, Measurement

admin.site.register(Sensor)
admin.site.register(Measurement)
