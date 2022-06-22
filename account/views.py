from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserLoginSerializer, UserDetailSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

class UserCreateAPIView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserLoginAPIView(APIView):	
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
       data = request.data
       serializer = UserLoginSerializer(data=data)
       if serializer.is_valid(raise_exception=True):
           new_data = serializer.data
       	   return Response(new_data, status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	 

class UserDetailAPIView(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserDetailSerializer

