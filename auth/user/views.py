from rest_framework.response import Response
from django.shortcuts import render
from .serializer import *

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token

class LoginAPI(APIView):
    def post(self,request):
        try:
            data = request.data
            serializer = LoginSerializer(data = data)
            if serializer.is_valid():
                school_id = serializer.data['school_id']
                phone_number = serializer.data['phone_number']
                username = serializer.data['username']
                password = serializer.data['password']

                user = authenticate(school_id =school_id,phone_number=phone_number,username=username,password=password)
                if user is None:
                     return Response({
                        'status' : 400,
                        'message': 'invalid password',
                        'data': {}
                    })
                refesh = RefreshToken.for_user(user)
                return Response({
                    'refresh' : str(refesh),
                    'data': str(refesh.access_token),
                })
            
            return Response({
                        'status' : 400,
                        'message': 'something went wrong',
                        'data': serializer.errors
                    })
        
        except:
            return Response({
                        'status' : 400,
                        'message': 'something went wrong',
                        'data': serializer.errors
                    })

