from libs.rss_reader import send_to_telegram
from libs.rss_fetch import get_rss_feed
from libs.settings import twitch_channel
import time
import os

# call the functions to get twtich videos
get_rss_feed(twitch_channel)

# send the URLs to telegram
take_file = open('libs/urls.rss' , 'r')
# print(take_file.readlines())
for i in take_file.readlines():
    # print(i)
    send_to_telegram('/VideoDownloadBot '+i)
    # time.sleep(1)

# remove the RSS files 
if os.path.exists("libs/feed.rss"):
  os.remove("libs/feed.rss")
else:
  print("The file does not exist")
if os.path.exists("libs/urls.rss"):
  os.remove("libs/urls.rss")
else:
  print("The file does not exist")