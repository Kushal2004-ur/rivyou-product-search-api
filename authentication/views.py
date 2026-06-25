from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import RegisterSerializer
from drf_yasg.utils import swagger_auto_schema


class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
    request_body=RegisterSerializer,
    operation_summary="Register User",
    operation_description="Register a new user account."
)

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response(
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "message": "User registered successfully",
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(TokenObtainPairView):
    permission_classes = [AllowAny]