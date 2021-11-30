from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.welcome_message_api),
    path('request_db', views.get_requested_db),
    path('get_all_dbs', views.get_all_dbs),
    path('get_meta_db_info', views.get_meta_db_info),
    path('update_record', views.update_record),
    path('add_record', views.add_record),
    path('remove_record', views.remove_record),
    path('test_view', views.test_view)
]