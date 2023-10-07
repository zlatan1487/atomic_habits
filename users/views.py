from rest_framework import generics
from rest_framework import permissions
from users.models import User
from users.serializers import CustomUserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]
