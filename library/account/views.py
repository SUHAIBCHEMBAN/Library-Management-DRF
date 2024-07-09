from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .userserializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User


class UserRegistrationView(generics.CreateAPIView):
    """
    API view for user registration.

    This view provides a POST method to create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            'Your Login Successful! Welcome Our Library!!!'
        )

#TODO : ADD THE CUSTOM RESPONSE MESSAGE AFTER USER LOGIN 


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom serializer for JWT token obtainment.

    This serializer customizes the token response to include the username.
    """
    def validate(self, attrs):
        """
        Validates the input data and returns the token along with the username.
        """
        data = super().validate(attrs)
        data.update({'user': self.user.username})
        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    API view for obtaining JWT token pairs.

    This view provides a POST method to obtain a JWT token pair (access and refresh tokens).
    """
    serializer_class = CustomTokenObtainPairSerializer
