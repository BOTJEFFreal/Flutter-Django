import os
from django.conf import settings
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import *
from .serializer import *

@api_view(['GET'])
def DocumentListCreateAPIView(request):
    data = Document.objects.all()
    serializer = DocumentSerializer(data,many=True)
    return(Response(serializer.data))

@api_view(['POST'])
def add_image(request):
    # Get the uploaded image file
    print(request.data)
    serializer = ImageSerializer(data = request.data['file'][0])
    if(serializer.is_valid()):
        serializer.save()
        return Response({'message': 'Image added successfully.'})
    return Response(serializer.errors)

class DocumentCreateAPIView(generics.CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
class ChildCreateAPIView(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class DocumentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class ImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
