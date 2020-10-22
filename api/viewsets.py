from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, viewsets, filters, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer, CommentSerializer
from .models import Project, Task, Comment
import time

@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        print(self.request.data)
        serializer.save(user=self.request.user)

    #api/project/retrieve/ funciona
    def retrieve(self, request, *args, **kwargs):
        user = User.objects.get(username=self.request.user)
        project = Project.objects.filter(user=user)
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def retrieve(self, request, *args, **kwargs):
        project = Project.objects.get(id=self.request.data['id'])
        task = Task.objects.filter(project=project)
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def retrieve(self, request, *args, **kwargs):
        task = Task.objects.get(id=self.request.data['id'])
        comment = Comment.objects.filter(task=task)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GetAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        try:
            response = super(GetAuthToken, self).post(request, *args, **kwargs)
            token = Token.objects.get(key=response.data['token'])
            user = User.objects.get(id=token.user_id)
            user_serializer = UserSerializer(user, many=False)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        except:
            response = {'message': 'usuario o contraseña no valido'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

def binary_gap(n):
    if n.isdecimal() and int(n)>0:
        elementos = bin(int(n))[2:].strip('0').split('1')
        return len(max(elementos))
    else:
        return "el valor ingresado no es valido"

class Test_One(APIView):
    #permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            data = request.data['entero']
            start = time.time()
            data = binary_gap(data)
            end = time.time()
            return Response({'respuesta': data, 'tiempo de ejecucion': end-start}, status=status.HTTP_200_OK)
        except:
            response = {'message': 'not found'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)