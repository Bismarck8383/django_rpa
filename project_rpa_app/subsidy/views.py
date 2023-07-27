
from django.shortcuts import render
import requests
from django.http import JsonResponse
from datetime import date, timedelta


def api_view(request):
    page_number = int(request.GET.get('page', 1))  # Obtener el número de página actual de los parámetros de la URL
    limit = 50  # Número de subsidios a obtener por página

    # Calcular el índice de inicio para la página actual
    start_index = (page_number - 1) * limit

    # Construir la URL de la API con los parámetros de paginación
    url = f'https://api-rpa.apps.bosonit.com/subsidies?skip={start_index}&limit={limit}'

    # Realizar la solicitud GET a la API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        total_subsidies = data["total"]  # Obtener el número total de subsidios en la respuesta
        subsidies = data["data"]  # Obtener la lista de subsidios

        total_pages = (total_subsidies // limit) + 1  # Calcular el número total de páginas

        # Ventana de paginación
        pages_to_show = 10
        pages_to_skip = pages_to_show // 2

        page_range_start = max(1, page_number - pages_to_skip)
        page_range_end = min(total_pages + 1, page_number + pages_to_skip + 1)
        page_range = range(page_range_start, page_range_end)
        location_name = "Spain"

        today = date.today()
        yesterday = today - timedelta(days=1)
        new_records = sum(1 for subsidy in subsidies if subsidy.get("registration_date") == str(today))
        new_records_yesterday = sum(1 for subsidy in subsidies if subsidy.get("registration_date") == str(yesterday))

        return render(request, 'index.html', {
            'data': subsidies,  # Devuelve los subsidios directamente
            'current_page': page_number,
            'total_pages': total_pages,
            'page_range': page_range,
            'location_name': location_name,
            'total': total_subsidies,
            'new_records': new_records,
            'hoy': today,
            'new_records_yesterday': new_records_yesterday
        })
    else:
        return render(request, 'error.html')


def bdns_filter_id(request):
    bdns_like = request.GET.get('bdns__like', '')  # Aquí recoges el valor introducido por el usuario

    url = f'https://api-rpa.apps.bosonit.com/subsidies?skip=0&limit=1&bdns__like={bdns_like}'  # Aquí añades el valor a la llamada a la API

    # Definimos un valor por defecto para subsidy
    subsidy = []

    # Realizar la solicitud GET a la API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        subsidy = data["data"]  # Obtener la lista de subsidios

    return JsonResponse({'subsidy': subsidy})


def get_locations(request):
    response = requests.get('https://api-rpa.apps.bosonit.com/locations')
    locations = response.json().get('data', [])

    return JsonResponse(locations, safe=False)


def subsidies_location(request, location, loc_name):
    if request.method == 'GET':
        page_number = int(request.GET.get('page', 1))  # Obtener el número de página actual de los parámetros de la URL
        limit = 50  # Número de subsidios a obtener por página

        # Calcular el índice de inicio para la página actual
        start_index = (page_number - 1) * limit

        # Construir la URL de la API con los parámetros de paginación y ubicación
        url = f'https://api-rpa.apps.bosonit.com/subsidies?skip={start_index}&limit={limit}&location={location}'

        # Realizar la solicitud GET a la API
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            total_subsidies = data["total"]  # Obtener el número total de subsidios en la respuesta
            subsidies = data["data"]  # Obtener la lista de subsidios

            total_pages = (total_subsidies // limit) + 1  # Calcular el número total de páginas

            # Ventana de paginación
            pages_to_show = 10
            pages_to_skip = pages_to_show // 2

            page_range_start = max(1, page_number - pages_to_skip)
            page_range_end = min(total_pages + 1, page_number + pages_to_skip + 1)
            page_range = range(page_range_start, page_range_end)

            today = date.today()
            yesterday = today - timedelta(days=1)
            new_records = sum(1 for subsidy in subsidies if subsidy.get("registration_date") == str(today))
            new_records_yesterday = sum(
                1 for subsidy in subsidies if subsidy.get("registration_date") == str(yesterday))

            return render(request, 'index.html', {
                'data': subsidies,  # Devuelve los subsidios directamente
                'current_page': page_number,
                'total_pages': total_pages,
                'page_range': page_range,
                'total': total_subsidies,
                'location_name': loc_name,
                'new_records': new_records,
                'hoy': today,
                'new_records_yesterday': new_records_yesterday

            })
        else:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')


def subsidies_bdns_like(request, bdns):
    if request.method == 'GET':
        page_number = int(request.GET.get('page', 1))  # Obtener el número de página actual de los parámetros de la URL
        limit = 50  # Número de subsidios a obtener por página

        # Calcular el índice de inicio para la página actual
        start_index = (page_number - 1) * limit

        # Construir la URL de la API con los parámetros de paginación y ubicación
        url = f'https://api-rpa.apps.bosonit.com/subsidies?skip={start_index}&limit={limit}&bdns__like={bdns}%25'
        # Realizar la solicitud GET a la API
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            total_subsidies = data["total"]  # Obtener el número total de subsidios en la respuesta
            subsidies = data["data"]  # Obtener la lista de subsidios

            total_pages = (total_subsidies // limit) + 1  # Calcular el número total de páginas

            # Ventana de paginación
            pages_to_show = 10
            pages_to_skip = pages_to_show // 2

            page_range_start = max(1, page_number - pages_to_skip)
            page_range_end = min(total_pages + 1, page_number + pages_to_skip + 1)
            page_range = range(page_range_start, page_range_end)
            location_name = "Spain"

            today = date.today()
            yesterday = today - timedelta(days=1)
            new_records = sum(1 for subsidy in subsidies if subsidy.get("registration_date") == str(today))
            new_records_yesterday = sum(
                1 for subsidy in subsidies if subsidy.get("registration_date") == str(yesterday))

            return render(request, 'index.html', {
                'data': subsidies,  # Devuelve los subsidios directamente
                'current_page': page_number,
                'total_pages': total_pages,
                'page_range': page_range,
                'location_name': location_name,
                'total': total_subsidies,
                'new_records': new_records,
                'hoy': today,
                'new_records_yesterday': new_records_yesterday

            })
        else:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')


def subsidies_bdns_like_location(request, bdns, location, loc_name):
    if request.method == 'GET':
        page_number = int(request.GET.get('page', 1))  # Obtener el número de página actual de los parámetros de la URL
        limit = 50  # Número de subsidios a obtener por página

        # Calcular el índice de inicio para la página actual
        start_index = (page_number - 1) * limit

        # Construir la URL de la API con los parámetros de paginación y ubicación
        url = f'https://api-rpa.apps.bosonit.com/subsidies?skip={start_index}&limit={limit}&bdns__like={bdns}%25&location={location}'
        # Realizar la solicitud GET a la API
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            total_subsidies = data["total"]  # Obtener el número total de subsidios en la respuesta
            subsidies = data["data"]  # Obtener la lista de subsidios

            total_pages = (total_subsidies // limit) + 1  # Calcular el número total de páginas

            # Ventana de paginación
            pages_to_show = 10
            pages_to_skip = pages_to_show // 2

            page_range_start = max(1, page_number - pages_to_skip)
            page_range_end = min(total_pages + 1, page_number + pages_to_skip + 1)
            page_range = range(page_range_start, page_range_end)

            today = date.today()
            yesterday = today - timedelta(days=1)
            new_records = sum(1 for subsidy in subsidies if subsidy.get("registration_date") == str(today))
            new_records_yesterday = sum(
                1 for subsidy in subsidies if subsidy.get("registration_date") == str(yesterday))

            return render(request, 'index.html', {
                'data': subsidies,  # Devuelve los subsidios directamente
                'current_page': page_number,
                'total_pages': total_pages,
                'page_range': page_range,
                'total': total_subsidies,
                'location_name': loc_name,
                'new_records': new_records,
                'hoy': today,
                'new_records_yesterday': new_records_yesterday

            })
        else:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')


def subsidies_title_like(request, title):
    if request.method == 'GET':
        page_number = int(request.GET.get('page', 1))  # Obtener el número de página actual de los parámetros de la URL
        limit = 50  # Número de subsidios a obtener por página

        # Calcular el índice de inicio para la página actual
        start_index = (page_number - 1) * limit

        # Construir la URL de la API con los parámetros de paginación y ubicación
        url = f'https://api-rpa.apps.bosonit.com/subsidies?skip={start_index}&limit={limit}&title__like={title}%25'
        # Realizar la solicitud GET a la API
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            total_subsidies = data["total"]  # Obtener el número total de subsidios en la respuesta
            subsidies = data["data"]  # Obtener la lista de subsidios

            total_pages = (total_subsidies // limit) + 1  # Calcular el número total de páginas

            # Ventana de paginación
            pages_to_show = 10
            pages_to_skip = pages_to_show // 2

            page_range_start = max(1, page_number - pages_to_skip)
            page_range_end = min(total_pages + 1, page_number + pages_to_skip + 1)
            page_range = range(page_range_start, page_range_end)
            location_name = "Spain"

            today = date.today()
            yesterday = today - timedelta(days=1)
            new_records = sum(1 for subsidy in subsidies if subsidy.get("registration_date") == str(today))
            new_records_yesterday = sum(
                1 for subsidy in subsidies if subsidy.get("registration_date") == str(yesterday))

            return render(request, 'index.html', {
                'data': subsidies,  # Devuelve los subsidios directamente
                'current_page': page_number,
                'total_pages': total_pages,
                'page_range': page_range,
                'location_name': location_name,
                'total': total_subsidies,
                'new_records': new_records,
                'hoy': today,
                'new_records_yesterday': new_records_yesterday

            })
        else:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')


# Subsidios por presupuesto
def subsidies_budget_like(request, budget):
    if request.method == 'GET':
        page_number = int(request.GET.get('page', 1))  # Obtener el número de página actual de los parámetros de la URL
        limit = 100  # Número de subsidios a obtener por página

        # Convertir el valor del presupuesto a un número de punto flotante
        budget_float = float(budget)

        # Calcular el índice de inicio para la página actual
        start_index = (page_number - 1) * limit

        # Construir la URL de la API con los parámetros de paginación y el presupuesto
        url = f'https://api-rpa.apps.bosonit.com/subsidies?skip={start_index}&limit={limit}&budget={budget_float}'

        # Realizar la solicitud GET a la API
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            total_subsidies = data["total"]  # Obtener el número total de subsidios en la respuesta
            subsidies = data["data"]  # Obtener la lista de subsidios

            total_pages = (total_subsidies // limit) + 1  # Calcular el número total de páginas

            # Ventana de paginación
            pages_to_show = 10
            pages_to_skip = pages_to_show // 2

            page_range_start = max(1, page_number - pages_to_skip)
            page_range_end = min(total_pages + 1, page_number + pages_to_skip + 1)
            page_range = range(page_range_start, page_range_end)

            return render(request, 'index.html', {
                'data': subsidies,  # Devuelve los subsidios directamente
                'current_page': page_number,
                'total_pages': total_pages,
                'page_range': page_range,
                'total': total_subsidies
            })
        else:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')






