from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv
import urllib.parse

from pagination.settings import BUS_STATION_CSV


def index():
    return redirect(reverse('bus_stations'))


with open(BUS_STATION_CSV, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    bus_stations_list = []
    for row in reader:
        bus_stations_list.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})


def bus_stations(request):

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stations_list, 10)
    page = paginator.get_page(page_number)
    data = page.object_list

    base_url = f'{reverse(bus_stations)}?'
    if page.has_next():
        params = urllib.parse.urlencode({'page': page_number + 1})
        next_page_url = base_url + params
    else:
        next_page_url = None
    if page.has_previous():
        params = urllib.parse.urlencode({'page': page_number - 1})
        prev_page_url = base_url + params
    else:
        prev_page_url = None

    context = {
        'bus_stations': data,
        'current_page': page_number,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    }

    return render(request, 'stations/index.html', context)
