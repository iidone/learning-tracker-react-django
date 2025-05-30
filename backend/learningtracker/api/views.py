from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import Users, Ideas
from .serializers import UsersSerializer
import json

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


@api_view(['POST'])
def add_idea(request):
    try:
        data = json.loads(request.body)
        user = get_object_or_404(Users, id=data.get('user_id'))


        idea = Ideas.objects.create(
            title=data.get('title', ''),
            theme=data.get('theme', ''),
            description=data.get('description', ''),
            user_id=user
        )

        users = Users.objects.all()

        return Response({
            'status': 'success',
            'idea_id': idea.id,
            'users_count': users.count()
        }, status=201)
        
    except Exception as e:
        return Response({
            'status': 'error',
            'message': str(e)
        }, status=400)