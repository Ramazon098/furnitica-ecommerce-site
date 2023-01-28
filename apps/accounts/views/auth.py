from django.contrib.auth import (
    authenticate, login, logout,
)

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from knox.auth import AuthToken
from apps.accounts.serializers import (
    RegisterSerializer, LoginSerializer,
)


# Create your views here.

class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if request.user.is_authenticated:
            return Response({
                "login_error": "To register from the system, you must first log out.",
            }, status=status.HTTP_401_UNAUTHORIZED)

        if serializer.is_valid():
            user = serializer.save()
            _, token = AuthToken.objects.create(user)

            return Response({
                'user': serializer.data,
                'token': token,
            }, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request},
        )

        if request.user.is_authenticated:
            return Response({
                "login_error": "You must log out before logging in.",
            }, status=status.HTTP_401_UNAUTHORIZED)

        if serializer.is_valid():
            user = authenticate(
                request=request,
                username=request.data['email'],
                password=request.data['password'],
            )

            if user is not None:
                login(request, user)
                _, token = AuthToken.objects.create(user)

                return Response({
                    'user': serializer.data,
                    'token': token,
                }, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        user = request.user
        logout(request)

        token = AuthToken.objects.filter(user=user)
        token.delete()

        return Response({
            "logout_success": "You have successfully logged out.",
        }, status=status.HTTP_204_NO_CONTENT)
