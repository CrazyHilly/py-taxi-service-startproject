# Generated by Django 5.1.1 on 2024-09-15 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0002_alter_car_manufacturer"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="driver",
            options={"verbose_name": "Driver"},
        ),
    ]
