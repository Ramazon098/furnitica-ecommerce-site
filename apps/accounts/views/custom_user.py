from rest_framework.generics import ListAPIView, RetrieveAPIView

from rest_framework.response import Response
from rest_framework import status

from apps.accounts.models import CustomUser
from apps.accounts.serializers import CustomUserSerializer


# Create your views here.

class CustomUserAPIView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_superuser:
            return Response({
                "login_error": "You must log out to get a list of users.",
            }, status=status.HTTP_401_UNAUTHORIZED)

        return super().list(request, *args, **kwargs)


class CustomUserRetrieveAPIView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
