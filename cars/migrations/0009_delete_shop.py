# Generated by Django 4.2.2 on 2023-06-06 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_remove_car_shop'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Shop',
        ),
    ]
