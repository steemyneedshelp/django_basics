from django.shortcuts import render # type: ignore
from .models import movie
from .serializers import MovieSerializer , MovieSerializerCustom
from rest_framework import generics # pyright: ignore[reportMissingImports]
from rest_framework.permissions import IsAuthenticated # pyright: ignore[reportMissingImports]

class MovieListView(generics.ListAPIView):
  queryset = movie.objects.all()
  serializer_class = MovieSerializer
  permission_class = [IsAuthenticated]

class MovieListCreate(generics.CreateAPIView):
   queryset = movie.objects.all()
   serializer_class = MovieSerializer
   permission_class = [IsAuthenticated]

class MovieListRetrieve(generics.RetrieveAPIView):
   queryset = movie.objects.all()
   serializer_class = MovieSerializer
   permission_class = [IsAuthenticated]

class MovieListUpdate(generics.UpdateAPIView):
   queryset = movie.objects.all()
   serializer_class = MovieSerializer
   permission_class = [IsAuthenticated]

class MovieListDelete(generics.DestroyAPIView):
   queryset = movie.objects.all()
   serializer_class = MovieSerializer
   permission_class = [IsAuthenticated]