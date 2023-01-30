import os

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
    blog_comment = CommentSerializer(read_only=True, many=True)

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

    def validate_images(self, value):
        extensions = os.path.splitext(value.name)[1]
        validate_extensions = ['.jpg', '.png', '.jpeg', '.gif', '.raw']

        if not extensions.lower() in validate_extensions:
            raise serializers.ValidationError({
                'extension_error': 'You can only upload images here.',
            })

        return value
