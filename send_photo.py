import requests
import os
TOKEN = os.getenv("TOKEN")

def send_photo(chat_id, photo_file):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    params={
        "chat_id":chat_id
    }
    files={

        "photo":photo_file
    }
    response = requests.post(url,params=params ,files=files)
    return response.json()
chat_id=6824726862
with open("image.png", "rb") as photo_file:
    response = send_photo(chat_id, photo_file)
    print(response)

