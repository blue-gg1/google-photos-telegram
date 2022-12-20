import os
import requests
import time
from settings import twitch_video_regex, twitch_video_id_regex, rss_file_name
from secrets import bot_name, tele_chatID, tele_api_token

# define the function
def send_to_telegram(message):
    # build the URL with the secret API key
    apiURL = f'https://api.telegram.org/bot{tele_api_token}/sendMessage'
    try:
        # send the request 
        response = requests.post(apiURL, json={'chat_id': tele_chatID, 'text': message})
        # tell me what happened 
        print(response.status_code)
        print(response.text)
    except Exception as e:
        print(e)