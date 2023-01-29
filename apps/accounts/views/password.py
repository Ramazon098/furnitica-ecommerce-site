from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from pyotp import HOTP

from apps.accounts.models import CustomUser, Otp
from apps.accounts.permissions import NotIsAuthenticated
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
            }, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendCodeAPIView(APIView):
    permission_classes = [NotIsAuthenticated,]
    serializer_class = SendCodeSerializer

    def post(self, request):
        email = request.data['email']
        serializer = self.serializer_class(
            data=request.data,
        )

        if serializer.is_valid():
            serializer.save()

            try:
                user = CustomUser.objects.get(email=email)
                hotp = HOTP(email)
                random_otp = hotp.at(user.id)

                try:
                    otp_user = Otp.objects.get(user=user)
                    otp_user.otp = random_otp
                    otp_user.save()
                except Otp.DoesNotExist:
                    _ = Otp.objects.create(user=user, otp=random_otp)

                send_mail(
                    "Your account verification email.",
                    f"Your otp is: {random_otp}.",
                    settings.EMAIL_HOST_USER,
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
    permission_classes = [NotIsAuthenticated,]
    serializer_class = VerifyOtpSerializer

    def post(self, request):
        otp = request.data['otp']
        serializer = self.serializer_class(
            data=request.data,
        )

        if serializer.is_valid():
            serializer.save()

            try:
                otp = Otp.objects.get(otp=otp)
                user = otp.user
                hotp = HOTP(user.email)

                if hotp.verify(otp.otp, user.id):
                    current_site = get_current_site(request=request).domain
                    relative_link = reverse('reset-password', kwargs={'pk': user.id})
                    absolute_url = current_site + relative_link
                else:
                    pass

                return Response({
                    "verify_otp": "Execute the api request given below.",
                    "api": absolute_url,
                }, status=status.HTTP_200_OK)
            
            except Otp.MultipleObjectsReturned:
                pass

            except Otp.DoesNotExist:
                return Response({
                    "not_found": "The code you entered did not match the code sent to your email.",
                }, status=status.HTTP_404_NOT_FOUND)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordAPIView(APIView):
    permission_classes = [NotIsAuthenticated,]
    serializer_class = ResetPasswordSerializer

    def put(self, request, pk):
        serializer = self.serializer_class(
            data=request.data,
        )

        if serializer.is_valid():
            serializer.save()

            try:
                user = CustomUser.objects.get(pk=pk)
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
