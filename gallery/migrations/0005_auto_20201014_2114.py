# Generated by Django 2.2 on 2020-10-14 18:14

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20201011_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_path',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]
