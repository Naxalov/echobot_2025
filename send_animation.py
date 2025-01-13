import requests
import os
TOKEN = os.getenv("TOKEN")

def send_animation(chat_id, animation_file_path):
    url = f"https://api.telegram.org/bot{TOKEN}/sendAnimation"
    files = {
        'animation': animation_file_path
    }
    params={
        'chat_id': chat_id
    }
    response = requests.post(url, files=files, params=params)
    return response.json()
chat_id=6824726862
print(send_animation(chat_id, ""))