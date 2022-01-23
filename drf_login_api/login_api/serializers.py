from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only':True}
        }
    def create(self, validated_data):
        password = validated_data['password']
        instance = self.Meta.model(**validated_data)
        print("password is none")
        if password is not None:
            instance.set_password(password)
        instance.save()
        Profile(user=instance, username=validated_data['username'], email=validated_data['email'])
        return instance
