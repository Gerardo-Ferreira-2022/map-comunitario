from django.shortcuts import render
import folium
from folium.plugins import HeatMap
from .models import Task
import random
# Create your views here.

def generate_random_locations():
    # Coordenadas aproximadas de Santiago de Chile
    latitudes = [-33.5, -33.3]  # Rango de latitudes dentro de Santiago
    longitudes = [-70.75, -70.45]  # Rango de longitudes dentro de Santiago
    locations = []

    for _ in range(50):  # Crear 50 ubicaciones aleatorias
        lat = random.uniform(latitudes[0], latitudes[1])
        lon = random.uniform(longitudes[0], longitudes[1])
        locations.append((lat, lon))
    
    return locations

# Vista index
def index(request):
    # Definir el mapa centrado en Chile
    initialMap = folium.Map(location=[-33.45694, -70.64827], zoom_start=8)

    # Lista de coordenadas de los campus INACAP en Chile
    inacap_locations = [
        {"name": "INACAP Santiago Centro", "coords": [-33.4623, -70.6500]},
        {"name": "INACAP Maipú", "coords": [-33.4874, -70.8320]},
        {"name": "INACAP Puente Alto", "coords": [-33.6110, -70.5720]},
        {"name": "INACAP Vicuña Mackenna", "coords": [-33.4558, -70.6296]},
        {"name": "INACAP Ñuñoa", "coords": [-33.4644, -70.6155]},
        {"name": "INACAP San Bernardo", "coords": [-33.5991, -70.6095]},
        {"name": "INACAP Concepción", "coords": [-36.8272, -73.0477]},
        {"name": "INACAP Valparaíso", "coords": [-33.0361, -71.5510]},
        {"name": "INACAP Antofagasta", "coords": [-23.6557, -70.3959]},
        {"name": "INACAP La Serena", "coords": [-29.9045, -71.2507]},
        {"name": "INACAP Temuco", "coords": [-38.7389, -72.6007]},
        {"name": "INACAP Puerto Montt", "coords": [-41.4709, -72.9443]}
    ]

    # Agregar un marcador para cada campus de INACAP
    for location in inacap_locations:
        folium.Marker(
            location["coords"],
            popup=location["name"]
        ).add_to(initialMap)

    # Retornar el mapa como un objeto HTML
    context = {'map': initialMap._repr_html_()}
    return render(request, 'index.html', context)


# Vista menu.
def menu(request):


    # Defino el mapa
    initialMap = folium.Map(location=[-33.45694, -70.64827], zoom_start=11)

  
    context = {'map':initialMap._repr_html_()}
    return render(request, 'menu.html', context)
