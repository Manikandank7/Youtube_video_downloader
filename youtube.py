from __future__ import unicode_literals
import youtube_dl
from time import sleep

url=input("video_url:")
ydl_opts = {} 
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    while True:
        try:
            ydl.download([url])
            break
        except Exception as e :
            print(e)
            print("Retrying. . .")
            sleep(5)
