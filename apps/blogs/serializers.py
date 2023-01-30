from rest_framework import serializers

from apps.blogs.models import Blog, Comment


# Create your serializers here.

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


class BlogSerializer(serializers.ModelSerializer):
    blog_comment = CommentSerializer(many=True)

    class Meta:
        model = Blog
        fields = [
            'id',
            'author',
            'title', 
            'body',
            'images',
            'blog_comment',
            'created_at',
            'updated_at',
        ]
