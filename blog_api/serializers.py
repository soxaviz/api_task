from rest_framework import serializers
from .models import Task, Comment
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class TaskListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'status',
            'due_date',
            'user',
        ]


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = [
            'id',
            'task',
            'author',
            'text',
            'created_at',
        ]


class TaskDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    comments = CommentSerializer(many=True)

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'status',
            'due_date',
            'created_at',
            'updated_at',
            'user',
            'comments',
        ]
