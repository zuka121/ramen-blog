# Generated by Django 5.0.6 on 2024-10-01 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0004_store_image_store_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='prefecture',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
