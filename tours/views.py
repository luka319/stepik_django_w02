from django.shortcuts import render
# Create your views here.
import random
from tours.data import title, subtitle, description, tours

def main_view(request):
    random_tours = dict(random.sample(tours.items(), 6))
    return render(request, "tours/index.html", context={
        'title':title,
        'subtitle':subtitle,
        'description':description,
        'tours': random_tours,
    } )


def departure_view(request, departure):

    return render(request, "tours/departure.html", )


def tour_view(request, id_):

    return render(request, "tours/tour.html", )

from django.http import HttpResponse, HttpResponseNotFound

def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')