from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.accounts.models import CustomUser
from apps.accounts.serializers import CustomUserSerializer


# Create your views here.

class CustomUserAPIView(APIView):
    serializer_class = CustomUserSerializer

    def get(self, request):
        custom_users = CustomUser.objects.all()
        serializer = self.serializer_class(instance=custom_users, many=True)

        if request.user.is_authenticated and not request.user.is_superuser:
            return Response({
                "login_error": "You must log out to get a list of users.",
            }, status=status.HTTP_401_UNAUTHORIZED)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CustomUserRetrieveAPIView(APIView):
    serializer_class = CustomUserSerializer

    def get(self, request, pk):
        custom_user = CustomUser.objects.get(pk=pk)
        serializer = self.serializer_class(instance=custom_user)

        if request.user.is_authenticated and not request.user.is_superuser:
            return Response({
                "login_error": "You must log out to retrieve user information.",
            }, status=status.HTTP_401_UNAUTHORIZED)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
