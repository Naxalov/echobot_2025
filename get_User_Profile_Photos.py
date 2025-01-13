import requests
import os
from pprint import pprint
import send_photo
TOKEN = os.environ['TOKEN'] 

def get_user_profile_photos(user_id: int):
    URL = f'https://api.telegram.org/bot{TOKEN}/getUserProfilePhotos'
    response = requests.get(URL, params={'user_id': user_id})
    return response.json()


user_id = 6824726862
pprint(get_user_profile_photos(user_id))

