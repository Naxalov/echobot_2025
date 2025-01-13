import requests
import os
TOKEN = os.getenv("TOKEN")

def sendPoll(chat_id, question, options):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPoll"
    data = {
        "chat_id": chat_id,
        "question": question,
        "options": options
    }
    response = requests.post(url, json=data)
    return response.json()

print(sendPoll(chat_id=6824726862, question="What is your favorite color?", options=["Red", "Green", "Blue"]))