from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response 

class TestView(APIView):

    def get(self, request, *args, **kwargs):
        data = {
            'data': 'Today',
            'key': '83V3o@@kopkdq@#$pood'
        }
        return Response(data)
