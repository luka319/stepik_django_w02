from django.shortcuts import render
# Create your views here.
# from django.http import HttpResponse
from django.http import HttpResponseNotFound
import random
from tours.data import title, subtitle, description, departures, tours


def main_view(request):
    random_tours = dict(random.sample(tours.items(), 6))
    return render(request, "tours/index.html", context={
        'title': title,
        'subtitle': subtitle,
        'description': description,
        'tours': random_tours,
        'departures': departures,
    })


def departure_view(request, departure):

    dep = departures[departure]
    # dep2 = "/departures/"+dep+"/"
    count = 0
    prices = []
    nights = []

    for val01 in tours.values():
        # print(f"{val01=}")
        for ke, va in val01.items():
            if va == departure:

                prices.append(val01['price'])
                nights.append(val01['nights'])
                count += 1

    prices_max = max(prices)
    prices_min = min(prices)
    nights_max = max(nights)
    nights_min = min(nights)
    return render(request, "tours/departure.html", context={
        # 'title':title,
        # 'subtitle':subtitle,
        # 'description':description,
        # 'tours': random_tours,
        'tours': tours,
        'departures': departures,
        'departure': departure,
        'dep': dep,
        'count': count,
        'prices_min': prices_min,
        'prices_max': prices_max,
        'nights_min': nights_min,
        'nights_max': nights_max,
    })


def tour_view(request, id_):
    # tours = data.tours
    # departures = data.departures

    for key, val01 in tours.items():
        if key == int(id_):
            for ke, va in val01.items():
                if ke == "title":
                    title = va
                if ke == "stars":
                    stars = "★" * int(va)
                if ke == "country":
                    country = va
                if ke == "price":
                    price = va
                if ke == "picture":
                    picture = va
                if ke == "nights":
                    nights = va
                if ke == "description":
                    description = va
                if ke == "departure":
                    departure2 = va
                    departure1 = departures[va]

    return render(request, "tours/tour.html", context={
        'title': title, 'tours': tours,
        'stars': stars, 'price': price,
        'country': country, 'picture': picture,
        'nights': nights, 'departure2': departure2,
        'departure1': departure1,
        'description': description, 'departures': departures
    })


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')
