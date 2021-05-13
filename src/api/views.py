from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
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
get_model_names
Function to return name of models in Django DB
@Param: -
@Return: JSON object with informations about name of models in Django DB fetched from serializers.py
"""
@api_view(["GET"])
def get_model_names(request):
    return Response(serializers.serializer_prepare_model_names())