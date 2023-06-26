import os
from django.conf import settings
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Image
from .serializer import ImageSerializer

@api_view(['GET'])
def get_images(request,name):
    data = Image.objects.filter(name__startswith=name)
    serializer = ImageSerializer(data,many = True)
    return(Response(serializer.data))
    # folder_path = os.path.join(settings.MEDIA_ROOT, folder_name)
    # print(folder_path)
    # # Retrieve image objects from the database
    # images = Image.objects.filter(file__startswith=folder_path)

    # # Generate the URLs for each image file
    # image_urls = [request.build_absolute_uri(image.file.url) for image in images]

    # return JsonResponse({'images': image_urls})

@api_view(['POST'])
def add_image(request,):
    # Get the uploaded image file
   
    serializer = ImageSerializer(data = request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response({'message': 'Image added successfully.'})
    return Response(serializer.errors)

