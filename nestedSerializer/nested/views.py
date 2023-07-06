from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import FirstModel
# Create your views here.

def current_datetime(request):
    html = "<html><body>It is now %s.</body></html>" % 5
    return HttpResponse(html)



class NestedDataView(APIView):
    def get(self, request):
        queryset = FirstModel.objects.all()
        serializer = FirstLevelSerializer(queryset, many=True)
        return Response(serializer.data)
