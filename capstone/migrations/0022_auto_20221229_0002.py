# Generated by Django 3.1.7 on 2022-12-29 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0021_parking_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='img_src',
            field=models.FileField(max_length=200, upload_to='static/capstone/'),
        ),
    ]
