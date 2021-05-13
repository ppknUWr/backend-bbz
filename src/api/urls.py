from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_message_api),
    path('request_db', views.get_requested_db),
    path('get_all_dbs', views.get_all_dbs)
]