# Generated by Django 2.2 on 2020-03-18 09:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('outdoorx', '0013_auto_20200318_0723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='location_images',
        ),
        migrations.AddField(
            model_name='location',
            name='docfile',
            field=models.FileField(default=django.utils.timezone.now, upload_to='documents/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
