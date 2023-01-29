from django.db import models
from django.contrib.auth import get_user_model

from apps.validators import validate_image_extension
CustomUser = get_user_model()


# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='blog_post',
        verbose_name='Custom Users',
    )

    title = models.CharField(
        max_length=128,
        verbose_name='Blog Title',
    )

    body = models.TextField(
        verbose_name='Blog Body',
    )

    images = models.FileField(
        upload_to='images/',
        validators=[validate_image_extension],
        verbose_name='Blog Image',
    )

    created_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        verbose_name='Blog Post Create',
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        verbose_name='Blog Post Update',
    )

    def __str__(self):
        return self.title

    @property
    def comments(self):
        instance = self
        return Comment.objects.filter(blog=instance)


class Comment(models.Model):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='user_comment',
        verbose_name='Custom User',
    )

    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='blog_comment',
        verbose_name='Blog Posts',
    )

    name = models.CharField(
        max_length=128,
        verbose_name='Comment Name',
    )

    email = models.EmailField(
        max_length=128,
        verbose_name='Comment Email',
    )

    website = models.URLField(
        max_length=128,
        verbose_name='Comment Website',
    )

    message = models.TextField(
        verbose_name='Comment Message',
    )

    created_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        verbose_name='Blog Post Create',
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        verbose_name='Blog Post Update',
    )

    def __str__(self):
        return self.name
