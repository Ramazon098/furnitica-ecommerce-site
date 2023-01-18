from django.contrib.auth import logout

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

from knox.auth import AuthToken


# Create your views here.

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        user = request.user
        logout(request)

        token = AuthToken.objects.filter(user=user)
        token.delete()

        return Response({
            "logout_success": "You have successfully logged out.",
        }, status=status.HTTP_204_NO_CONTENT)
