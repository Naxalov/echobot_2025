import requests
import os
TOKEN = os.getenv("TOKEN")

def send_audio(chat_id, audio_file_path):
    url = f"https://api.telegram.org/bot{TOKEN}/sendAudio"
    params= {
        "chat_id": chat_id,
    }
    files = {
        "audio":audio_file_path
    }
    response = requests.post(url, params=params, files=files)
    return response.json()
with open("audio.mp3", "rb") as audio_file:
    response = send_audio(chat_id=6824726862, audio_file_path=audio_file)
    print(response)