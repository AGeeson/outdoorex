# Generated by Django 2.2.8 on 2020-05-18 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outdoorx', '0029_auto_20200518_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(upload_to='attachments', verbose_name='Attachment'),
        ),
    ]
