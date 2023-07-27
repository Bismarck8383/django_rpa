import requests
from django.shortcuts import render


def api_view(request):
    # Realizar la solicitud GET a la API
    response = requests.get('')

    # Verificar el estado de la respuesta
    if response.status_code == 200:
        # Convertir los datos de la respuesta en formato JSON
        data = response.json()

        # Renderizar la página y pasar los datos a la plantilla
        return render(request, 'tender.html', {'data': data})
    else:
        # Manejar el caso de error de la solicitud
        return render(request, 'error.html')
