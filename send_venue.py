import requests
import os
TOKEN = os.getenv("TOKEN")

def send_venue(chat_id, latitude, longitude, title, address):
    url = f"https://api.telegram.org/bot{TOKEN}/sendVenue"
    params = {
        "chat_id": chat_id,
        "latitude": latitude,
        "longitude": longitude,
        "title": title,
        "address": address
    }
    response = requests.post(url, params=params)
    return response.json()
print(send_venue(chat_id=6824726862, latitude=39.675209, longitude=66.935077, title="My house", address="Samarkand regions,Bagdod street,23"))