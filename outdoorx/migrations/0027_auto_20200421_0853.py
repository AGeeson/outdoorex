# Generated by Django 3.0.4 on 2020-04-21 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outdoorx', '0026_auto_20200419_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='image',
            field=models.ImageField(default='/pic_folder/None/no-img.jpg', upload_to='pic_folder'),
        ),
    ]
