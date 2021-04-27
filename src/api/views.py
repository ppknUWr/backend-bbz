from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
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