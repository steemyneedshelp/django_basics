from rest_framework import serializers
from .models import movie

class MovieSerializer(serializers.ModelSerializer):
  class Meta:
    model = movie
    fields = '__all__'

class MovieSerializerCustom(serializers.ModelSerializer):
  class Meta:
    model = movie
    fields = ['title', 'active']    