# Generated by Django 2.2 on 2020-03-19 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoorx', '0017_auto_20200319_0107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='text',
            new_name='title',
        ),
    ]
