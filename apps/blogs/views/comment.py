from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status

from apps.blogs.models import Comment
from apps.blogs.serializers import CommentSerializer


# Create your views here.

class CommentAPIView(APIView):
    serializer_class = CommentSerializer

    def get(self, request):
        comments = Comment.objects.all()
        serializer = self.serializer_class(
            instance=comments,
            many=True,
        )

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data,
        )

        if serializer.is_valid():
            serializer.save()

            if not request.user.is_authenticated:
                return Response({
                    'blog_error': 'You want to create a blog, you need to register.',
                }, status=status.HTTP_401_UNAUTHORIZED)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailAPIView(APIView):
    serializer_class = CommentSerializer

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise NotFound("The requested comment could not be found.")

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = self.serializer_class(instance=comment)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        blog = self.get_object(pk)
        serializer = self.serializer_class(
            instance=blog,
            data=request.data,
        )

        if serializer.is_valid():
            serializer.save()

            if not request.user.is_authenticated:
                return Response({
                    'blog_error': 'You want to create a blog, you need to register.',
                }, status=status.HTTP_401_UNAUTHORIZED)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        blog = self.get_object(pk)
        serializer = self.serializer_class(
            instance=blog,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()

            if not request.user.is_authenticated:
                return Response({
                    'blog_error': 'You want to create a blog, you need to register.',
                }, status=status.HTTP_401_UNAUTHORIZED)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = self.get_object(pk)
        blog.delete()

        if not request.user.is_authenticated:
            return Response({
                'blog_error': 'You want to create a blog, you need to register.',
            }, status=status.HTTP_401_UNAUTHORIZED)

        return Response(status=status.HTTP_204_NO_CONTENT)
