from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, Task, Comment

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'user']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('__all__')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


