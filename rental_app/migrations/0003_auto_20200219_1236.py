# Generated by Django 3.0.3 on 2020-02-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0002_auto_20200219_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owned_cars',
            name='car_image',
            field=models.ImageField(upload_to='car_pics'),
        ),
    ]
