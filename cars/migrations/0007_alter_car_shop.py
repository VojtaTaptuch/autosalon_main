# Generated by Django 4.2.2 on 2023-06-06 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_car_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='shop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cars.shop', verbose_name='Prodejna'),
        ),
    ]
