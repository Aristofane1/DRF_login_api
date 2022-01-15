from rest_framework import serializers
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'status']
        extra_kwargs = {
            'password': {'write_only':True}
        }
    def create(self, validated_data):
        password = validated_data['password']
        instance = self.Meta.model(**validated_data)
        print("password is non")
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance