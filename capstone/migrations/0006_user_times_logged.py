# Generated by Django 3.1.7 on 2022-12-20 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0005_auto_20221219_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='times_logged',
            field=models.IntegerField(null=True),
        ),
    ]
