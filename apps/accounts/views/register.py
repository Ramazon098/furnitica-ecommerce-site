from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from knox.auth import AuthToken

from apps.accounts.serializers import RegisterSerializer


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

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
