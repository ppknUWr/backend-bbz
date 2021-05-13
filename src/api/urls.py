from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_message_api),
    path('db_names', views.get_model_names)
]