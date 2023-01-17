from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from apps.accounts.serializers import EditProfileSerializer


# Create your views here.

class EditProfileAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = EditProfileSerializer

    def put(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request},
        )

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)