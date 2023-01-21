# Generated by Django 4.1.4 on 2023-01-21 14:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_address_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(max_length=5, null=True, validators=[django.core.validators.RegexValidator('^[0-9]{5}$', 'Invalid postal code.')], verbose_name='Zip Code'),
        ),
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^[0-9]{5}$', 'Invalid postal code.')], verbose_name='One-time password')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='otp', to=settings.AUTH_USER_MODEL, verbose_name='Custom Users')),
            ],
        ),
    ]
