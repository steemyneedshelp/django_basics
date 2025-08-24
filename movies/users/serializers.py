from rest_framework import serializers # type: ignore
from .models import theUser

class UserRegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = theUser
    fields = ['username', 'email', 'password', 'role']

  def validate(self, data):
      if data['username'] == data['password']:
        raise serializers.ValidationError("don't use your username as a password, please")
      return data
    
  def create(self, validated_data):
      user= theUser.objects.create_user(
        username= validated_data['username'],
        email=validated_data['email'],
        password=validated_data['password'],
        role=validated_data['role']
      )
      return user
  
class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model = theUser
      fields = ['username', 'email', 'id']

class UserSerializerNoID(serializers.ModelSerializer):
   class Meta:
      model = theUser
      fields = ['username', 'email']