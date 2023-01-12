from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from knox.auth import AuthToken

from apps.accounts.serializers import ChangePasswordSerializer


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

            _, token = AuthToken.objects.create(user)

            return Response({
                "password_success": "Your password has been successfully changed.",
                'token': token,
            }, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
