from rest_framework import serializers

from apps.blogs.models import Blog, Comment


# Create your serializers here.

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'id',
            'title', 
            'body',
            'image',
        ]


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'name',
            'email',
            'website',
            'message',
        ]
