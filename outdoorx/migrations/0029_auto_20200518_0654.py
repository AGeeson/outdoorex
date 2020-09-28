# Generated by Django 2.2.8 on 2020-05-18 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outdoorx', '0028_auto_20200518_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(upload_to='pic_folder'),
        ),
        migrations.AlterField(
            model_name='location',
            name='file',
            field=models.FileField(upload_to='pic_folder'),
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='pic-folder', verbose_name='Attachment')),
                ('location', models.ForeignKey(on_delete='PROTECT', to='outdoorx.Location', verbose_name='Location')),
            ],
        ),
    ]
