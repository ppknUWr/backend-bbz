from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.welcome_message_api),
    path('request_db', views.get_requested_db),
    path('get_all_dbs', views.get_all_dbs),
    path('db_names', views.get_db_names),
    path('update_record', views.update_record)
]