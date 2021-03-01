from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'date': 'Today',
            'key': 'test_key_304'
        }
        return Response(data)
