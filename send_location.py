import requests
import os
TOKEN = os.getenv("TOKEN")

def send_location(chat_id, latitude, longitude):
    url = f"https://api.telegram.org/bot{TOKEN}/sendLocation"
    
    
    params = {
        "chat_id": chat_id,
        "latitude": latitude,
        "longitude": longitude
    }
    response = requests.post(url, params=params)
    return response.json()  
print(send_location(chat_id=6824726862, latitude=39.675209, longitude=66.935077))