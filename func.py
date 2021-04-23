import youtube_dl
import sys


def youtube_download_interface(url, setting):
    ydl_opts = {
        "format": "bestaudio/best",
        # If you want to download all the specify the playliststar to 1 and playlistend to the len of the playlist
        "playliststart": 1,
        "playlistend": None,
        "playlist_items": None,  # or this value can be None if you don't want to specify a playlist_items
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    if setting == None:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
           ydl.extract_info(url, download=False)
    elif ":" in setting:
        print("Portion")
        temp = setting[1:-1].split(":")
        ydl_opts["playliststart"] = int(temp[0])
        ydl_opts["playlistend"] = int(temp[1])
        # print(ydl_opts)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=False)
    elif "," in setting:
        filtered_list = filter(lambda x: x != "", setting[1:-1].split(","))
        playlist_items_list = list(filtered_list)
        playlist_items_str = ",".join(map(str, playlist_items_list))
        ydl_opts["playlist_items"] = playlist_items_str
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=False)
        # GET assets of each video in a playlist
        # for video in info_dict["entries"]:
        #     print()
        #     if not video:
        #         print("ERROR: Unable to get info. Continuing...")
        #         continue
        #     for property in ["thumbnail", "id", "title", "webpage_url"]:
        #         print(property, "--", video.get(property))


    # ******************************** SINGLE VIDEO ********************************************************
    # GET URL of video
    # info_dict['webpage_url']

    # GET Thumbnail of video
    # info_dict['thumbnail']

    # GET Title of a single video
    # title = info_dict['title']
    # print(title)
