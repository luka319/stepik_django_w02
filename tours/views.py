from django.shortcuts import render
# Create your views here.
import random
from tours.data import title, subtitle, description, departures, tours

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
        'title': title,
        'tours': tours,
        'stars': stars,
        'price': price, 'country':country, 'picture': picture,
        'nights': nights, 'departure2': departure2,
        'departure1':departure1,
        'description': description, 'departures': departures
    })

    # return render_template("tour.html",tours=tours, title=title, stars=stars,
    #         price=price, country=country,picture=picture,nights=nights, departure=departure,
    #         description=description,
    #         departures=departures)




from django.http import HttpResponse, HttpResponseNotFound

def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')