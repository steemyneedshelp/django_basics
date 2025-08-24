from django.shortcuts import render # type: ignore
from .serializers import *
from .models import theUser
from rest_framework import generics # type: ignore
from rest_framework.permissions import IsAuthenticated # type: ignore
from .permissions import IsStaff

class UserRegisterCreate(generics.CreateAPIView):
  queryset = theUser.objects.all()
  serializer_class = UserRegisterSerializer

class UserListView(generics.ListAPIView):
  queryset = theUser.objects.all()
  serializer_class = UserSerializerNoID
  permission_classes = [IsAuthenticated, IsStaff]

class UserDetailView(generics.RetrieveAPIView):
  queryset = theUser.objects.all()
  serializer_class = UserRegisterSerializer
  permission_classes = [IsAuthenticated, IsStaff]

class UserUpdateView(generics.UpdateAPIView):
  queryset = theUser.objects.all()
  serializer_class = UserSerializerNoID
  permission_classes = [IsAuthenticated, IsStaff]

class UserDeleteView(generics.DestroyAPIView):
  queryset = theUser.objects.all()
  serializer_class = UserRegisterSerializer 
  permission_classes = [IsAuthenticated, IsStaff]