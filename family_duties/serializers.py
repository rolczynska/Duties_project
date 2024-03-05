from rest_framework import serializers
from .models import Category, Task


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class TaskSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'category', 'created', 'author',
                  'assigned_to']
