from django.urls import path
from .views import index, populate_step

urlpatterns = [
    path('', index, name='index'),
    path('populate-step/', populate_step, name='populate_step'),
]
