from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.accounts import serializers

from apps.accounts.models import CustomUser
from apps.accounts.serializers import (
    SendCodeSerializer,
    VerifyOtpSerializer,
    ResetPasswordSerializer,
)


# Create your views here.

class SendCodeAPIView(APIView):
    serializer_class = SendCodeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']

        if serializer.is_valid():
            serializer.save()

            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return Response({
                    "not_found": "This email has not been registered with our system.",
                }, status=status.HTTP_404_NOT_FOUND)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOtpAPIView(APIView):
    serializer_class = VerifyOtpSerializer

    def get(self, request):
        pass


class ResetPasswordAPIView(APIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        pass
