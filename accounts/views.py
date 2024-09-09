from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializers




class Login(TokenObtainPairView):
    pass

class Refresh(TokenRefreshView):
    pass

class SingIN(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def perform_create(self, serializer):
        user = User.objects.create_user(username=serializer.validated_data['username'],
                                        password=serializer.validated_data['password'])
        return user

