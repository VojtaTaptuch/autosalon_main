from django.db import models


class Type(models.Model):
    engine = models.CharField(max_length=50,
                              verbose_name='Typ motoru',
                              help_text='Zadejte typ motoru vozidla - např. spalovací, elektro')
    etype = models.CharField(max_length=100,
                             verbose_name='Bližší specifikace motoru',
                             null=True,
                             blank=True,
                             help_text='Zadejte specifikace motoru vozidla - např. dvouválec, objem')
    doors = models.PositiveIntegerField(default=5,
                              verbose_name='Počet dveří vozidla',
                              help_text='Zadejte číslo odpovídající k počtu dveří vozidla')

    class Meta:
        verbose_name = 'Typ'
        verbose_name_plural = 'Typy'
        ordering = ['-doors']

    def __str__(self):
        return self.engine


class Shop(models.Model):
    cars_capacity = models.PositiveIntegerField(default=10,
                                      verbose_name='Kapacita prodejny',
                                      help_text='Zadejte maximální kapacitu prodejny')
    city = models.CharField(max_length=80,
                            verbose_name='Město',
                            help_text='Zadejte název obce')
    street = models.CharField(max_length=80,
                              verbose_name='Ulice',
                              help_text='Zadejte název ulice + číslo')

    psc = models.PositiveIntegerField(verbose_name='PSČ',
                            null=True,
                            blank=True,
                            help_text='Zadejte poštovní směrovací číslo')

    class Meta:
        verbose_name = 'Prodejna'
        verbose_name_plural = 'Prodejny'
        ordering = ['-cars_capacity']

    def __str__(self):
        return f'{self.city} ,{str(self.street)}'


class Customer(models.Model):
    role = models.CharField(max_length=80,
                            verbose_name='Role zákazníka',
                            help_text='Zadejte roli zákazníka - např. prodávající, nakupující')
    note = models.TextField(max_length=100,
                            verbose_name='Poznámka',
                            null=True,
                            blank=True,
                            help_text='Zadejte poznámku k zákazníkovi')

    class Meta:
        verbose_name = 'Zákazník'
        verbose_name_plural = 'Zákazníci'

    def __str__(self):
        return self.role


class Car(models.Model):
    brand = models.CharField(max_length=60,
                             verbose_name='Značka vozidla',
                             help_text='Zadejte značku auta - např. Škoda Octavia, Audi quattro')
    y_of_manufacture = models.PositiveIntegerField(verbose_name='Rok výroby',
                                         null=True,
                                         blank=True,
                                         help_text='Zadejte rok výroby auta')
    mileage = models.FloatField(verbose_name='Počet najetých km',
                                help_text='Zadejte počet najetých km vozidla')

    price = models.FloatField(verbose_name='Cena',
                              help_text='Zadejte cenu auta')

    type = models.ForeignKey(Type,
                             verbose_name='Typ',
                             on_delete=models.CASCADE,
                             )

    shop = models.ForeignKey(Shop,
                             null=True,
                             verbose_name='Prodejna',
                             on_delete=models.CASCADE,
                             )

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Auta'
        ordering = ['-price']

    def __str__(self):
        return f'{self.brand} ({str(self.y_of_manufacture)})'
