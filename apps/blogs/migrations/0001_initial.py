# Generated by Django 4.1.4 on 2023-01-30 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Blog Title')),
                ('body', models.TextField(verbose_name='Blog Body')),
                ('images', models.FileField(upload_to='images/', verbose_name='Blog Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Blog Post Create')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Blog Post Update')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_post', to=settings.AUTH_USER_MODEL, verbose_name='Custom Users')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Comment Name')),
                ('email', models.EmailField(max_length=128, verbose_name='Comment Email')),
                ('website', models.URLField(max_length=128, verbose_name='Comment Website')),
                ('message', models.TextField(verbose_name='Comment Message')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Blog Post Create')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Blog Post Update')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL, verbose_name='Custom User')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_comment', to='blogs.blog', verbose_name='Blog Posts')),
            ],
        ),
    ]
