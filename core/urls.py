from django.urls import path
from core.views import index, user_ui


app_name = 'core'

urlpatterns = [
    path("", index, name="index"),
    path('user_ui', user_ui , name='user_ui'),
]
