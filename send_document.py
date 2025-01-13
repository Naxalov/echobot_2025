import requests
import os
TOKEN = os.getenv("TOKEN")

def send_document(chat_id,document):
    url=f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    params={
        "chat_id":chat_id,
        
    }
    files={
        "document":document
    }
    response=requests.post(url,params=params,files=files)
    return response.json()
chat_id=6824726862
with open("main.csv","rb") as file:
   print(send_document(chat_id,file))

