from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.accounts.models import CustomUser
from apps.accounts.permissions import NotIsAuthenticated
from apps.accounts.serializers import (
    CustomUserSerializer, EditProfileSerializer,
)


# Create your views here.

class CustomUserAPIView(APIView):
    permission_classes = [NotIsAuthenticated,]
    serializer_class = CustomUserSerializer

    def get(self, request):
        custom_users = CustomUser.objects.all()
        serializer = self.serializer_class(
            instance=custom_users,
            many=True,
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CustomUserRetrieveAPIView(APIView):
    serializer_class = CustomUserSerializer

    def get(self, request, pk):
        try:
            custom_user = CustomUser.objects.get(pk=pk)
            serializer = self.serializer_class(
                instance=custom_user,
            )

            if request.user.is_authenticated and not request.user.is_superuser:
                return Response({
                    "login_error": "You must log out to retrieve user information.",
                }, status=status.HTTP_401_UNAUTHORIZED)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        except CustomUser.DoesNotExist:
            return Response({
                "not_found": "The requested user was not found.",
            }, status=status.HTTP_404_NOT_FOUND)


class EditProfileAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = EditProfileSerializer

    def get(self, request):
        serializer = self.serializer_class(
            instance=request.user,
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        serializer = self.serializer_class(
            instance=request.user,
            data=request.data,
        )

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        serializer = self.serializer_class(
            instance=request.user,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
