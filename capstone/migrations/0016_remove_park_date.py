# Generated by Django 3.1.7 on 2022-12-23 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0015_park'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='park',
            name='date',
        ),
    ]