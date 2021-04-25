import youtube_dl
import sys
import csv


def write_csv(video, backup_title):

    with open(
        "data/info/mp3_download_history/" + backup_title + ".csv", mode="a", newline="", encoding="utf-8"
    ) as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow(
            [video["id"], video["title"], video["thumbnail"], video["webpage_url"]]
        )
        quit()
    

def archive_video(ydl, info_dict):
    if not ydl.in_download_archive(info_dict):
                ydl.download([info_dict["webpage_url"]])
                ydl.record_download_archive(info_dict)
                backup_title = info_dict["title"].replace(" ", "_")
                for video in info_dict["entries"]:
                    print()
                    if not video:
                        print("ERROR: Unable to get info. Continuing...")
                        continue
                    write_csv(video, backup_title)

def youtube_download_interface(url, setting):
    ydl_opts = {
        "format": "bestaudio/best",
        # If you want to download all the specify the playliststar to 1 and playlistend to the len of the playlist
        "playliststart": 1,
        "playlistend": None,
        "playlist_items": None,  # or this value can be None if you don't want to specify a playlist_items
        "download_archive": "./data/info/log.txt",
        "outtmpl": "C:/Users/vuaba/Music/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    if setting == "mp3":
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            if not ydl.in_download_archive(info_dict):
                ydl.download([info_dict["webpage_url"]])
                ydl.record_download_archive(info_dict)
                write_csv(info_dict, "music_backup")
    elif setting == "playlist":
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            archive_video(ydl,info_dict)
    elif ":" in setting:
        print("Portion")
        temp = setting[1:-1].split(":")
        ydl_opts["playliststart"] = int(temp[0])
        ydl_opts["playlistend"] = int(temp[1])
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            archive_video(ydl,info_dict)
    elif "," in setting:
        filtered_list = filter(lambda x: x != "", setting[1:-1].split(","))
        playlist_items_list = list(filtered_list)
        playlist_items_str = ",".join(map(str, playlist_items_list))
        ydl_opts["playlist_items"] = playlist_items_str
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            archive_video(ydl,info_dict)
