import config
import os

def get_available_songs():
    available_files = []

    for file in os.listdir(config.MUSIC_DIR):
        extension = list(file.split("."))[-1]
        if extension == "mp3":
            available_files.append(file[:-4])

    if available_files == []:
        raise Exception("Error! No files available to play!")

    return available_files

def organize_songs(songs):
    artist_songs = {}

    for song in songs:
        parts = song.split(" - ")
        if len(parts) != 2:
            continue

        artists_part, song_title = parts

        artists = [artist.strip() for artist in artists_part.replace("&", ",").split(",")]

        for artist in artists:
            if artist not in artist_songs:
                artist_songs[artist] = []
                
            if song_title not in artist_songs[artist]:
                artist_songs[artist].append(song_title)

    return artist_songs

if __name__ == "__main__":  
    import json
    result = get_available_songs()
    print(json.dumps(result, indent=2, ensure_ascii=False))
