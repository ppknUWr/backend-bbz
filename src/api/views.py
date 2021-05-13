from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.apps import apps
import datetime
# Create your views here.

@api_view(["GET"])
def welcome_message_api(request):

    data = {
        "code": 1,
        "message": "API View Welcome Message",
        "timestamp": int(datetime.datetime.now().timestamp())
    }

    return Response(data)


@api_view(["GET"])
def get_requested_db(request):
    selected_db = request.query_params.get('db')
    db_exists = False
    for model in apps.all_models['api']:
        print(model)
        if(model == selected_db):
            db_exists = True

    if db_exists:
        data = {
            "code": 1,
            "message": "Your request: " + selected_db,
            "timestamp": int(datetime.datetime.now().timestamp())
        }
    else:
        data = {
            "code": 2,
            "message": "Error: DB does not exist !",
            "timestamp": int(datetime.datetime.now().timestamp())
        }
    return Response(data)


@api_view(["POST", "GET"])
def get_all_dbs(request):
    available_dbs = []
    i = 0
    for model in apps.all_models['api']:
        available_dbs.append({i : model})
        i += 1
        print(model)

    data = {
        "code": 1,
        "message": available_dbs,
        "timestamp": int(datetime.datetime.now().timestamp())
    }
    return Response(data)