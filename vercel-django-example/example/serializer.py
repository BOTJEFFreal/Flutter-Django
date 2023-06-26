from rest_framework import serializers
from .models import *
class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = ('id', 'image','created_at')

class DocumentSerializer(serializers.ModelSerializer):
    children = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Document
        fields = ('heading','sub_heading','content', 'children')

