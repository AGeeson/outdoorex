# Generated by Django 2.2.8 on 2020-05-19 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outdoorx', '0032_auto_20200519_0707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pic_folder')),
                ('location', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='images', to='outdoorx.Location')),
            ],
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
