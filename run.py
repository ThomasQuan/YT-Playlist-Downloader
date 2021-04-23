from __future__ import unicode_literals
from func import youtube_download_interface
import sys
import os

clear = lambda: os.system("clear")
try:
    option = sys.argv[1]
    if option.lower() == "download":
        url = sys.argv[2]
        formatType = url[(url.rfind("/") + 1) : (url.rfind("?"))]
        if formatType == "watch":
            youtube_download_interface(url, formatType)
        elif formatType == "playlist":
            pl_cmd = sys.argv[3]
            while True:
                if pl_cmd == "all":
                    print("download all")
                    youtube_download_interface(url, formatType, pl_cmd)
                    break
                elif pl_cmd == "portion":
                    print("download only a few section of the playlist")
                    youtube_download_interface(url, formatType, pl_cmd)
                    break
                elif pl_cmd == "select":
                    print("download only a selected few based on index ")
                    youtube_download_interface(url, formatType, pl_cmd)
                    break
                else:
                    pl_cmd = input("Wrong playlist cmd \n")
                    continue
        else:
            print("Wrong format")
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
        print("Invalid command")
except IndexError:
    clear()
    print(
        """   --- Wrong format ---
    Download a single video command: download url_link 
    Download a playlist command: download url_link [all?, portion?, select?] """
    )

# youtube_download_interface("https://www.youtube.com/watch?v=wMzUIZpAIYI")
