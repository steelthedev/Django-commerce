from django.shortcuts import render
from .serilizers import *
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, response
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser


from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )



class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer