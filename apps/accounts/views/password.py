from random import randint

from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.accounts.models import (
    CustomUser,
    Otp,
)
from apps.accounts.serializers import (
    ChangePasswordSerializer,
    SendCodeSerializer,
    VerifyOtpSerializer,
    ResetPasswordSerializer,
)


# Create your views here.

class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = ChangePasswordSerializer

    def put(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request},
        )

        if serializer.is_valid():
            user = serializer.save()
            update_session_auth_hash(request, user)

            return Response({
                "password_success": "Your password has been successfully changed.",
            }, status=status.HTTP_205_RESET_CONTENT)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendCodeAPIView(APIView):
    serializer_class = SendCodeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']

        if serializer.is_valid():
            serializer.save()

            try:
                user = CustomUser.objects.get(email=email)
                random_otp = randint(100000, 999999)

                while Otp.objects.filter(otp=random_otp).exists():
                    random_otp = randint(100000, 999999)

                if Otp.objects.filter(user=user).exists():
                    otp_user = Otp.objects.get(user=user)
                    otp_user.otp = random_otp
                    otp_user.save()
                else:
                    _ = Otp.objects.create(user=user, otp=random_otp)

                send_mail(
                    "Your account verification email.",
                    f"Your otp is: {random_otp}.",
                    'ramazon0619@gmail.com',
                    [email],
                )

                return Response({
                    "send_code": "The code has been successfully sent to your email.",
                }, status=status.HTTP_200_OK)

            except CustomUser.DoesNotExist:
                return Response({
                    "not_found": "This email has not been registered with our system.",
                }, status=status.HTTP_404_NOT_FOUND)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOtpAPIView(APIView):
    serializer_class = VerifyOtpSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        otp = request.data['otp']

        if serializer.is_valid():
            serializer.save()

            try:
                _ = Otp.objects.get(otp=otp)
                current_site = get_current_site(request=request).domain
                relative_link = reverse('reset-password', kwargs={'otp': otp})
                absolute_url = 'http://' + current_site + relative_link

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

    def put(self, request, otp):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            try:
                otp = Otp.objects.get(otp=otp)
                otp.otp = 30303
                otp.save()
                user = otp.user
                user.set_password(request.data['new_password'])
                user.save()

                return Response({
                    "password_success": "Your password has been successfully reset.",
                }, status=status.HTTP_200_OK)

            except Otp.DoesNotExist:
                return Response({
                    "not_found": "The code you entered did not match the code sent to your email.",
                }, status=status.HTTP_404_NOT_FOUND)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
