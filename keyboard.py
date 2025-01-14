import requests
import os
TOKEN = os.getenv("TOKEN")

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    button={
         'text': '📚Sozlar'

    }
    button2={
        'text': '👑Pro',
    }
    button3={
        'text': '😊Mashqlar'
    }
    button4={
        'text': '🎉Sertifikatlar'
    }
    button5={
        'text': '📌Bellashuv'
    }
    button6={
        'text': '📝Qollanmalar'
    }
    button7={
        'text':'🪒Sozlamalar'
    }
    ReplayKeyboardMarkup={
        'keyboard': [
            [button2],
            [button,button3,button4],
            [button5,button6],
            [button7]
        ]
    }
    params={
        'chat_id': chat_id,
        'text': text,
        "reply_markup": ReplayKeyboardMarkup
    
    }
    response = requests.post(url, json=params)
    return response.json()
chat_id = 6824726862
text = "Hello, this is a test message"
response = send_message(chat_id, text)
print(response)