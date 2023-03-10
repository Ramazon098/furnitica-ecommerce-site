from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status

from apps.blogs.models import Blog
from apps.blogs.serializers import BlogSerializer


# Create your views here.

class BlogPostAPIView(APIView):
    serializer_class = BlogSerializer

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = self.serializer_class(
            instance=blogs,
            many=True,
        )

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data,
        )

        if not request.user.is_authenticated:
            return Response({
                'blog_error': 'You want to create a blog, you need to register.',
            }, status=status.HTTP_401_UNAUTHORIZED)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetailAPIView(APIView):
    serializer_class = BlogSerializer

    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise NotFound("The requested blog post could not be found.")

    def get(self, request, pk):
        blog = self.get_object(pk)
        serializer = self.serializer_class(
            instance=blog,
        )

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        blog = self.get_object(pk)
        serializer = self.serializer_class(
            instance=blog,
            data=request.data,
        )

        if not request.user.is_authenticated:
            return Response({
                'blog_error': 'You want to create a blog, you need to register.',
            }, status=status.HTTP_401_UNAUTHORIZED)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        blog = self.get_object(pk)
        serializer = self.serializer_class(
            instance=blog,
            data=request.data,
            partial=True,
        )

        if not request.user.is_authenticated:
            return Response({
                'blog_error': 'You want to create a blog, you need to register.',
            }, status=status.HTTP_401_UNAUTHORIZED)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not request.user.is_authenticated:
            return Response({
                'blog_error': 'You want to create a blog, you need to register.',
            }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            blog = self.get_object(pk)
            blog.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
