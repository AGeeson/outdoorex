# Generated by Django 2.2.8 on 2020-05-18 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outdoorx', '0030_auto_20200518_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='multiimage',
            field=models.ImageField(blank=True, default='location_images/stock.png', null=True, upload_to='location_images/'),
        ),
    ]
