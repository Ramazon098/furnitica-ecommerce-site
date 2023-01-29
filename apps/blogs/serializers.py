from rest_framework import serializers

from apps.blogs.models import Blog, Comment


# Create your models here.

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = []
