from django import db
from django.shortcuts import render
import json
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
        if (title != "metadbinfo"):
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
get_db_names
Function to return name of models in Django DB
@Param: -
@Return: JSON object with informations about name of models in Django DB fetched from serializers.py
"""
@api_view(["GET"])
def get_db_names(request):
    data = {
        "code": 1,
        "message": serializers.serializer_prepare_model_names()
    }
    return Response(data)

"""
update_record
Function to update record in Django DB
@Param: request: Request OBJ -> Handle request, and JSON data of record that we want to update
@Param: db_id: Str -> ID of DB to update
@Param: record_id: Str -> ID of record to update
"""
@api_view(["PATCH"])
def update_record(request):
    try:
        db_id = int(request.query_params.get('db')) # TODO: Change query_params to db_id
    except (ValueError, TypeError) as exception:
        return Response({
            "code": 2,
            "message": "Error, no database id provided",
            "timestamp": str(int(datetime.datetime.now().timestamp()))
        })

    try:
        record_id = int(request.query_params.get('record')) # TODO: Change query_params to record_id
    except (ValueError, TypeError) as exception:
        return Response({
            "code": 2,
            "message": "Error, no record id provided",
            "timestamp": str(int(datetime.datetime.now().timestamp()))
        })

    response = serializers.serializer_update_record(db_id, record_id, request.data) # db_id and record_id need to be casted into integers.
    return Response(response)

# TODO: Add description here. 
@api_view(["POST"])
def add_record(request):
    req = json.loads(request.body)
    print(req) # TODO: Remove this print.
    #acquiring the data from json
    try:
        db_id = int(req['db_id'])
    except KeyError:
        return Response({
            "code" : 2,
            "message" : "Error, no database id provided",
            "timestamp" : str(int(datetime.datetime.now().timestamp()))
        })

    try:
        body = req['data']
    except KeyError:
        return Response({
            "code" : 2,
            "message" : "Error, no data in the record to be added",
            "timestamp" : str(int(datetime.datetime.now().timestamp()))
        })

    response = serializers.serializer_add_new_record(db_id, body)
    
    if response:
        return Response({
            "code" : 0,
            "message" : "Record added successfully",
            "timestamp" : str(int(datetime.datetime.now().timestamp()))
        })
    else:
        return Response({
            "code" : 2,
            "message" : "Invalid record provided by user",
            "timestamp" : str(int(datetime.datetime.now().timestamp()))
        })
