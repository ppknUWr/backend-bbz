from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.apps import apps
import datetime
import api.serializers as serializers
# Create your views here.0

"""
welcome_message_api
Test Function to check if API is UP
@Param: -
@Return: data: Dict -> dictionary with welcome message, code, and timestamp on server
"""
@api_view(["GET"])
def welcome_message_api(request):

    data = {
        "code": 1,
        "message": "API View Welcome Message",
        "timestamp": int(datetime.datetime.now().timestamp())
    }

    return Response(data)

"""
get_requested_db
Function to return data for requested DB from database
@Param: selected_db_id: string 
@Return: JSON object with data of selected DB from django model
"""
@api_view(["GET"])
def get_requested_db(request):
    selected_db = request.query_params.get('db')
    db_exists = False
    available_dbs = serializers.serializer_get_db_data(selected_db)
    # for model in apps.all_models['api']:
    #     print(model)
    #     if(model == selected_db):
    #         db_exists = True

    # if db_exists:
    #     data = {
    #         "code": 1,
    #         "message": "Your request: " + selected_db,
    #         "timestamp": int(datetime.datetime.now().timestamp())
    #     }
    # else:
    #     data = {
    #         "code": 2,
    #         "message": "Error: DB does not exist !",
    #         "timestamp": int(datetime.datetime.now().timestamp())
    #     }
    data = available_dbs
    return Response(data)

"""
get_all_dbs
Function to return data for all DBs from database 
@Param: -
@Return: JSON object with data of all DBs available from django models
"""
@api_view(["POST", "GET"])
def get_all_dbs(request):
    counter = len(apps.all_models['api'])
    dbs_data = []
    i = 0
    for title in apps.all_models['api']:
        db = serializers.serializer_get_db_data(i)
        dbs_data.append({title : db})
        i += 1
    # for model in apps.all_models['api']:
    #     available_dbs.append({i : model})
    #     i += 1
    #     print(model)

    data = {
        "code": 1,
        "message": dbs_data,
        "timestamp": int(datetime.datetime.now().timestamp())
    }
    return Response(data)
  
"""
get_model_names
Function to return name of models in Django DB
@Param: -
@Return: JSON object with informations about name of models in Django DB fetched from serializers.py
"""
@api_view(["GET"])
def get_model_names(request):
    return Response(serializers.serializer_prepare_model_names())

