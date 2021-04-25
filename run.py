from __future__ import unicode_literals
from ydl_func import youtube_download_interface
import sys
import os
import re
import requests


def check_if_video(url):
    YTformat = url[24 : url.rfind("?")]
    # if result.status_code == 200 OK else 400 == NOT OK
    if YTformat == "watch":
        return True
    else:
        return False



try:

    option = sys.argv[1]
    if option.lower() == "download":
        url = sys.argv[2]
        check_url = "https://www.youtube.com/oembed?format=json&url="+url
        if(requests.get(check_url).status_code == 200):
            try:
                setting = sys.argv[3]
                while True:
                    if (
                        setting.startswith("[")
                        and setting.endswith("]")
                        and setting.count(":") == 1
                        and re.match(r"^[1-9:[\]]+$", setting)
                    ):
                        youtube_download_interface(url, setting)
                        break
                    elif (
                        setting.startswith("[")
                        and setting.endswith("]")
                        and re.match(r"^[1-9,[\]]+$", setting)
                    ):
                        youtube_download_interface(url, setting)
                        break
                    elif setting.lower() == "latest" and check_if_video(url) == False:
                        youtube_download_interface(url, setting)
                        break
                    else:
                        setting = input("Wrong playlist cmd \n")
                        continue

            except IndexError:
                result = check_if_video(url)
                if(result):
                    youtube_download_interface(url, "mp3")
                else:
                    youtube_download_interface(url, "playlist")
        else:
            print("Valid Youtube video is require")  
    else:
        print(
            """ --- Command options --- 
        download url_link (note: for download playlist/video full)
        download url_link [portion?, select?] (note: for download playlist/video from selected start to end or specific indices) """
        )
except IndexError:
    print(
        """   --- Wrong format ---
    Download a single video command: download url_link 
    Download a playlist command: download url_link [portion?, select?] """
    )

# youtube_download_interface("https://www.youtube.com/watch?v=wMzUIZpAIYI")
