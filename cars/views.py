from django.shortcuts import render
from .models import Car, Customer, Shop


def index(request):
    num_cars = Car.objects.all().count()
    context = {
        'num_films': num_cars,
    }

    return render(request, 'index.html', context=context)
