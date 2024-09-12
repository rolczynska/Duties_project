from rest_framework_simplejwt.views import TokenObtainPairView
from profiles.models import User
from rest_framework import viewsets, permissions
from profiles.serializers import UserSerializer, MyTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # change permission for creating new user without auth

    def get_queryset(self):
        return super().get_queryset().prefetch_related('tasks')


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
