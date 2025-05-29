from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Users
from .serializers import UsersSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello from Django!"})