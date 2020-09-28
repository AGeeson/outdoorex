# Generated by Django 2.2.8 on 2020-06-02 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outdoorx', '0044_auto_20200602_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=18, max_digits=55, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=18, max_digits=55, null=True),
        ),
    ]
