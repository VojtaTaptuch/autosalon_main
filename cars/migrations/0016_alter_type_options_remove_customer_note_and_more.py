# Generated by Django 4.2.2 on 2023-06-22 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0015_alter_car_brand_alter_car_y_of_manufacture'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Typ', 'verbose_name_plural': 'Typy'},
        ),
        migrations.RemoveField(
            model_name='customer',
            name='note',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='role',
        ),
        migrations.RemoveField(
            model_name='type',
            name='doors',
        ),
        migrations.RemoveField(
            model_name='type',
            name='etype',
        ),
        migrations.AddField(
            model_name='car',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.customer', verbose_name='Zakazník'),
        ),
        migrations.AddField(
            model_name='car',
            name='doors',
            field=models.PositiveIntegerField(default=5, help_text='Zadejte číslo odpovídající k počtu dveří vozidla', verbose_name='Počet dveří vozidla'),
        ),
        migrations.AddField(
            model_name='car',
            name='etype',
            field=models.CharField(blank=True, help_text='Zadejte specifikace motoru vozidla - např. dvouválec, objem', max_length=100, null=True, verbose_name='Bližší specifikace motoru'),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(blank=True, help_text='Zadejte email zákazníka', max_length=60, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, help_text='Zadejte jméno zákazníka', max_length=80, null=True, verbose_name='Jméno'),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_n',
            field=models.FloatField(blank=True, help_text='Zadejte telefoní číslo zákazníka', null=True, verbose_name='Telefoní číslo'),
        ),
        migrations.AddField(
            model_name='customer',
            name='surname',
            field=models.CharField(blank=True, help_text='Zadejte příjmení zákazníka', max_length=80, null=True, verbose_name='Příjmení'),
        ),
        migrations.AddField(
            model_name='customer',
            name='y_of_birth',
            field=models.PositiveIntegerField(blank=True, help_text='Zadejte rok narození zákazníka', null=True, verbose_name='Rok narození'),
        ),
    ]