from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.welcome_message_api),
    path('db_names', views.get_model_names)
]