from __future__ import unicode_literals
from func import youtube_download_interface
import sys
import os
import re

clear = lambda: os.system("clear")
try:
    option = sys.argv[1]
    if option.lower() == "download":
        url = sys.argv[2]
        # formatType = url[(url.rfind("/") + 1) : (url.rfind("?"))]
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
                else:
                    setting = input("Wrong playlist cmd \n")
                    continue

        except IndexError:
            youtube_download_interface(url, None)
        # if formatType == "watch":
        # elif formatType == "playlist":
        #     pl_cmd = sys.argv[3]

        # else:
        #     print("Wrong format")
    elif sys.argv[1] == "list":
        print("list all downloaded title and url with thumbnail url")
    elif sys.argv[1] == "clear":
        url = sys.argv[2]
        while True:
            formatType = url[(url.rfind("/") + 1) : (url.rfind("?"))]
            if formatType == "playlist":
                print("delete all empty video from playlist")
                break
            else:
                url = input(
                    "Playlist not specify - please ensure that URL is a playlist \n"
                )
                continue
    else:
        print(
            """ --- Command options --- 
        download url_link?
        list 
        clear url_link? """
        )
except IndexError:
    clear()
    print(
        """   --- Wrong format ---
    Download a single video command: download url_link 
    Download a playlist command: download url_link [all?, portion?, select?] """
    )

# youtube_download_interface("https://www.youtube.com/watch?v=wMzUIZpAIYI")
