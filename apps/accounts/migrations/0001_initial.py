# Generated by Django 4.1.4 on 2023-01-29 13:03

from django.conf import settings
import django.contrib.auth.password_validation
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=128, unique=True, verbose_name='Email Address')),
                ('first_name', models.CharField(max_length=128, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=128, null=True, verbose_name='Last Name')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True, verbose_name='Mobile Number')),
                ('image', models.ImageField(null=True, upload_to='images/', verbose_name='Custom User Image')),
                ('password', models.CharField(max_length=128, validators=[django.contrib.auth.password_validation.validate_password], verbose_name='Password')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Custom User',
                'verbose_name_plural': 'Custom Users',
            },
        ),
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^[0-9]{6}$', 'Invalid postal code.')], verbose_name='One-time password')),
                ('secret_key', models.CharField(max_length=40, verbose_name='Random Base 32')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='otp', to=settings.AUTH_USER_MODEL, verbose_name='Custom Users')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256, null=True, verbose_name='Address')),
                ('city', models.CharField(max_length=128, null=True, verbose_name='City')),
                ('country', models.CharField(max_length=128, null=True, verbose_name='Country')),
                ('zip_code', models.CharField(max_length=5, null=True, validators=[django.core.validators.RegexValidator('^[0-9]{5}$', 'Invalid postal code.')], verbose_name='Zip Code')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to=settings.AUTH_USER_MODEL, verbose_name='Custom Users')),
            ],
        ),
    ]
