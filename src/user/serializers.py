from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        user= User.objects.create(username=validated_data['username'],email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()