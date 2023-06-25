from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import GetImage
from .serializers import GetImageSerializer

@api_view(['GET'])
def fetch_all_images(request):
    all_images = GetImage.objects.all()
    serializer = GetImageSerializer(all_images, many=True)
    return Response(serializer.data)
