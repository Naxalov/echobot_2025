import requests
import os
TOKEN = os.getenv("TOKEN")
import time



def get_updates():

    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    r = requests.get(url)
    return r.json()

def send_message(text, chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    r=requests.get(url)
    return r.json()


idx=0
while True:
    response=requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates")
    data=response.json()
    result=data["result"]
    last_update=result[-1]
    next_update_id=last_update["update_id"]
    if next_update_id!=idx:
        message=last_update["message"]
        chat_id=message["chat"]["id"]
        text=message["text"]
        send_message(text,chat_id)
    idx=next_update_id
    time.sleep(1)
