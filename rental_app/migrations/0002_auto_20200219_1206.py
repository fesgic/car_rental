# Generated by Django 3.0.3 on 2020-02-19 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owned_cars',
            name='make',
            field=models.CharField(max_length=100),
        ),
    ]