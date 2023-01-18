from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from apps.accounts.serializers import EditProfileSerializer
from apps.accounts.models import CustomUser


# Create your views here.

class EditProfileAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = EditProfileSerializer

    def put(self, request):
        custom_user = CustomUser.objects.get(pk=request.user.id)

        serializer = self.serializer_class(
            instance=custom_user,
            data=request.data,
        )

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        serializer = self.serializer_class(
            instance=request.user,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
