from django.urls import path, include
from .views import itie


app_name = 'itie'


urlpatterns = [
    path('courses/',itie, name='Itie'),

]
