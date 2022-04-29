import requests
def geocode(address):
    params={'q':address,'format':'json'}
    place=requests.get(f'https://nominatim.openstreetmap.org/search',params=params).json()
    return [place[0].get('lat'),place[0].get('lon')]
geocode("138 Kingsland Rd, London E2 8DY")
