from django.urls import path
from .views import SensorsList, SensorView, MeasurementView


urlpatterns = [
    path('sensors/', SensorsList.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]