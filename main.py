import requests
import os
TOKEN = os.getenv("TOKEN")



def get_updates():

    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    r = requests.get(url)
    return r.json()

def send_message(text, chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}"
    r=requests.get(url)
    return r.json()

CHAT_ID =6824726862
while True:
    response=requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates")
    data=response.json()
    result=data["result"]
    last_update=result[-1]
    text=last_update["message"]["text"]
    chat_id=last_update["message"]["chat"]["id"]
    text=data['result'][-1]['message']['text']
    send_message(text,chat_id)



