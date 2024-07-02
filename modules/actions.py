import webbrowser
from geopy.geocoders import Nominatim
import requests
from modules.text_to_speech import text_to_speech
from config.config import GOOGLE_API_KEY

def search_wikipedia(query):
    url = f"https://pt.wikipedia.org/wiki/{query}"
    webbrowser.open(url)

def open_youtube():
    url = "https://www.youtube.com"
    webbrowser.open(url)

def find_nearest_pharmacy():
    geolocator = Nominatim(user_agent="assistant")
    location = geolocator.geocode("seu endereço ou coordenadas")
    if location:
        latitude = location.latitude
        longitude = location.longitude
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=1500&type=pharmacy&key={GOOGLE_API_KEY}"
        response = requests.get(url)
        results = response.json().get('results', [])
        if results:
            pharmacy = results[0]
            name = pharmacy['name']
            address = pharmacy['vicinity']
            print(f"A farmácia mais próxima é {name} que fica em {address}.")
            text_to_speech(f"A farmácia mais próxima é {name} que fica em {address}.")
        else:
            print("Nenhuma farmácia encontrada por perto.")
            text_to_speech("Nenhuma farmácia encontrada por perto.")
    else:
        print("Não foi possível obter a localização.")
        text_to_speech("Não foi possível obter a localização.")
