from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.accounts.models import CustomUser, Otp
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
                random_otp = 111111
                Otp.objects.create(user=user, otp=random_otp)

                send_mail(
                    "Your account verification email.",
                    f"Your otp is: {random_otp}.",
                    email,
                )

                return Response({
                    "code_send": "The code has been successfully sent to your email.",
                }, status=status.HTTP_200_OK)

            except CustomUser.DoesNotExist:
                return Response({
                    "not_found": "This email has not been registered with our system.",
                }, status=status.HTTP_404_NOT_FOUND)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOtpAPIView(APIView):
    serializer_class = VerifyOtpSerializer

    def get(self, request):
        serializer = self.serializer_class(data=request.data)
        otp = request.data['otp']

        if serializer.is_valid():
            serializer.save()

            try:
                Otp.objects.get(otp=otp)
                current_site = get_current_site(request=request).domain
                realtive_link = reverse('reset-password', kwargs={'otp': otp})
                absolute_url = 'http://' + current_site + realtive_link

                return Response({
                    "verify_otp": "Execute the api request given below.",
                    "api": absolute_url,
                }, status=status.HTTP_200_OK)

            except Otp.DoesNotExist:
                return Response({
                    "not_found": "The code you entered did not match the code sent to your email.",
                }, status=status.HTTP_404_NOT_FOUND)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordAPIView(APIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "password_success": "Your password has been successfully reset.",
            }, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
