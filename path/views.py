from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

class PathList(APIView):
    def get(self, request, format=None):
        return HttpResponse("Not implemented yet.", status=501)

class ConnectNode(APIView):
    def post(self, request, format=None):
        return HttpResponse("Not implemented yet.", status=501)
