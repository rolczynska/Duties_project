from rest_framework import serializers
from .models import Category, Task


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class TaskSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    # this is used for nice representation who created this task - with name not id
    author = serializers.ReadOnlyField(source='author.username')
    # it can be done like that
    # author = UserSerializer(read_only=True)
    # assigned_to = UserSerializer(read_only=True, allow_null=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'category', 'created', 'author',
                  'assigned_to']



