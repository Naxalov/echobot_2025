import requests
import os
TOKEN = os.getenv("TOKEN")



def get_updates():

    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    r = requests.get(url)
    return r.json()

def send_message(text, chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {
        'chat_id': chat_id, 
        'text': text,
        'parse_mode': 'MarkdownV2'
        }
    r = requests.get(url, params=params)
    return r.json()


def send_photo(photo, chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    params = {
        'chat_id': chat_id, 
        'photo': photo
        }
    r = requests.get(url, params=params)
    return r.json()

def send_contact(chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendContact"
    params = {
        'chat_id': chat_id, 
        'phone_number': '+998933339899',
        'first_name': 'Zarif',
        'last_name': 'Naxalov',
    }
    r = requests.get(url, params=params)
    return r.json()

CHAT_ID = "86775091"

send_contact(CHAT_ID)