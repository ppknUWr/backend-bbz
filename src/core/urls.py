from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_message_core)
]
