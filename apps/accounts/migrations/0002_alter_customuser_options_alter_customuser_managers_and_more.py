# Generated by Django 4.1.4 on 2023-01-12 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Custom User', 'verbose_name_plural': 'Custom Users'},
        ),
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.IntegerField(max_length=5, null=True, verbose_name='Zip Code'),
        ),
    ]
