from rest_framework import serializers
from .models import *

class LoginSerializer(serializers.Serializer):
    school_id = serializers.CharField()
    phone_number = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

