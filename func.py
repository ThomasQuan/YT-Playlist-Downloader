import youtube_dl
import sys


def youtube_download_interface(url, formatType, setting="none"):
    ydl_opts = {
        "format": "bestaudio/best",
        # If you want to download all the specify the playliststar to 1 and playlistend to the len of the playlist
        # 'playliststart' : 1,
        # 'playlistend' : 3,
        'playlist_items' : '4,5', # or this value can be None if you don't want to specify a playlist_items
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        if formatType == "watch":
            ydl.download([url])
        if formatType == "playlist":
            info_dict = ydl.extract_info(url, download=False)
            # GET assets of each video in a playlist
            # for video in info_dict["entries"]:
            #     print()
            #     if not video:
            #         print("ERROR: Unable to get info. Continuing...")
            #         continue
            #     for property in ["thumbnail", "id", "title", "webpage_url"]:
            #         print(property, "--", video.get(property))

    # GET info of the video/playlist without downloading
    # info_dict = ydl.extract_info(url, download=False)

    # ******************************** SINGLE VIDEO ********************************************************
    # GET URL of video
    # info_dict['webpage_url']

    # GET Thumbnail of video
    # info_dict['thumbnail']

    # GET Title of a single video
    # title = info_dict['title']
    # print(title)

    # ******************************** PLAYLIST ********************************************************
