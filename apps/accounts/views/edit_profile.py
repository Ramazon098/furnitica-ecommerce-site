from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

from apps.accounts.serializers import EditProfileSerializer
from apps.accounts.models import CustomUser

from rest_framework.generics import RetrieveUpdateAPIView

# Create your views here.

# class EditProfileAPIView(RetrieveUpdateAPIView):
#     queryset = CustomUser.objects.all()
#     permission_classes = [IsAuthenticated,]
#     serializer_class = EditProfileSerializer

#     def update(self, instance, request):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)

#         if serializer.is_valid():
#             serializer.save()

#             return Response({"message":"mobile number updated successfully"})

#         return Response({"message":"failed"})


class EditProfileAPIView(APIView):
    # queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = EditProfileSerializer

    def put(self, request):
        custom_user = CustomUser.objects.get(pk=request.data['user'].id)
        serializer = self.serializer_class(
            instance=custom_user,
            data=request.data,
        )

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request):
    #     serializer = self.serializer_class(
    #         instance=request.user,
    #         data=request.data,
    #         partial=True,
    #     )

    #     if serializer.is_valid():
    #         serializer.save()

    #         return Response(data=serializer.data, status=status.HTTP_200_OK)

    #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
