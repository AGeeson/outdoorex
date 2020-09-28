# Generated by Django 2.2.8 on 2020-05-25 02:09

from django.db import migrations, models
import outdoorx.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('outdoorx', '0037_auto_20200520_0739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='location',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AddField(
            model_name='location',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='staticfiles/outdoorexlogo.png', upload_to=outdoorx.models.images_directory_path),
        ),
        migrations.DeleteModel(
            name='Attachment',
        ),
    ]
