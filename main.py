import requests
import os
TOKEN = os.getenv("TOKEN")



def get_updates():

    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    r = requests.get(url)
    return r.json()

def send_message(text, chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {'chat_id': chat_id, 'text': text}
    r = requests.get(url, params=params)
    return r.json()

CHAT_ID = "86775091"

TEXT ="""
Simple TEXT
Bold TEXT
"""

send_message(TEXT, CHAT_ID)

