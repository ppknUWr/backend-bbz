from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import datetime
# Create your views here.

"""
Welcome message endpoint
Return Welcome Message by GET method
@Param: request
"""

@api_view(["GET"])
def welcome_message_core(request):

    data = {
        "code": 1,
        "message": "Core View Welcome Message",
        "timestamp": int(datetime.datetime.now().timestamp())
    }

    return Response(data)