from rest_framework import serializers

from apps.blogs.models import Blog, Comment


# Create your serializers here.

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'id',
            'author',
            'title', 
            'body',
            'images',
            'created_at',
            'updated_at',
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'author',
            'blog',
            'name',
            'email',
            'website',
            'message',
            'created_at',
            'updated_at',
        ]
