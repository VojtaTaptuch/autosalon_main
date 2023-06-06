from django.contrib import admin
from .models import Type
from .models import Car
from .models import Shop
from .models import Customer

admin.site.register(Type)
admin.site.register(Car)
admin.site.register(Shop)
admin.site.register(Customer)
