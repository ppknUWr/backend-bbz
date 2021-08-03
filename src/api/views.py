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
@Param: selected_db_id: int 
@Return: JSON object with data of selected DB from django model
"""
@api_view(["GET"])
def get_requested_db(request):
    selected_db = request.query_params.get('db')
    db_exists = True if int(selected_db) < len(apps.all_models['api']) else False
    
    if db_exists:
        db_data = serializers.serializer_get_db_data(selected_db)
        data = {
            "code": 1,
            "message": db_data,
            "timestamp": int(datetime.datetime.now().timestamp())
        }
    else:
        data = {
            "code": 2,
            "message": "Error: DB does not exist !",
            "timestamp": int(datetime.datetime.now().timestamp())
        }
    
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

"""
update_record
Function to update record in Django DB
@Param: request: Request OBJ -> Handle request, and JSON data of record that we want to update
@Param: db_id: Str -> ID of DB to update
@Param: record_id: Str -> ID of record to update
"""
@api_view(["PATCH"])
def update_record(request):
    db_id = int(request.query_params.get('db'))
    record_id = int(request.query_params.get('record'))
    response = serializers.serializer_update_record(db_id, record_id, request.data) # db_id and record_id need to be casted into integers.
    return Response(response)