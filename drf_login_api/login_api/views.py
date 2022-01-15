from django.views import View
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class UserView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        return Response({   
            'message': 'User are login'
        })
    
        