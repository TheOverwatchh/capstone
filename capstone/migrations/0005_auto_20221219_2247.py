# Generated by Django 3.1.7 on 2022-12-19 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0004_delete_slot'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='free_slots',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='parking',
            name='slots',
            field=models.IntegerField(default=0),
        ),
    ]
