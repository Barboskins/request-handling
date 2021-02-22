from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open (settings.BUS_STATION_CSV) as f:
        f_read = csv.DictReader(f)
        paginator = Paginator(list(f_read), settings.PAG_BUS_STATION_PER_PAGE)
        page_number = int(request.GET.get('page',1))
        current_page = paginator.get_page(page_number)
        msg = current_page.object_list
        if current_page.has_next():
            next_page_url = current_page.next_page_number()
        else:
            next_page_url = None
        if current_page.has_previous():
            prev_page_url = current_page.previous_page_number()
        else:
            prev_page_url = None
    return render(request, 'index.html', context={
        'bus_stations': msg,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })


