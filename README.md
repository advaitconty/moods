# Moods - the custom music player
Have you ever felt down one day and wanted the least amount of friction in your room to start playing music? well, introduing moods, you best friend for this!

It runs on a couple basic GET and POST requests to help play music directly on your PC. There is also a mobile app (refer to the mobile_apps folder for code) which is basically a set of simple buttons

It's very adaptable, and picks up all the MP3s you have of your favourite songs!

## App
Check the app out at [moods-remastered](https://github.com/advaitconty/moods-remastered)

## Demo
***This demo does not use the parts mentioned below because they weren't delivered in time. Will be updated once the parts are here.***

[![Moods Demo](https://markdown-videos-api.jorgenkh.no/url?url=https%3A%2F%2Fyoutu.be%2FNUVO6ZB55nc)](https://youtu.be/NUVO6ZB55nc)

## If you wanna use this with AI...,
make sure you create a file called `api_key.py` that contains this:
```python
ANTHROPIC_AI_KEY = "Your API Key"
```
This app uses Claude for AI

## How do I make this my own?
The only things you will need to setup are the non-Python based dependencies for the requirements (check requirements.txt) and `config.py`. Here is an example `config.py` for you to use in creating your own one

```python
MUSIC_DIR = "/Users/conytadvait/Music" 
# Without the / at the end else it won't work!

KEY = "soote" 
# For security reasons, so your friends can't just randomly POST to it!

# Not required but up to you!
PLAYLISTS = {"wind down": ["C418 - Minecraft.mp3", 
                           "C418 - Sweden.mp3", 
                           "C418 - Mice On Venus.mp3",
                           "C418 - Subwoofer Lullaby.mp3",
                           "C418 - Wet Hands.mp3",
                           "C418 - Haggstrom.mp3"],
            "relax": ["BoyWithUke - I Wish.mp3",
                      "BoyWithUke - Animal Crackers.mp3",
                      "BoyWithUke - Nightmare.mp3",
                      "BoyWithUke - Blurry Nights.mp3"]}
```

Finally, if you wanna set up the mobile app to your own server, just change the server and password in settings!

(screenshot)

## Parts used
*All parts used are from LCSC or Hack Club*

1. UGREEN MicroUSB to OTG adapter (LCSC Part Number: C3014637)

2. UGREEN USB to Audio Jack External Sound Card (LCSC Part Number: C5222408)

3. Raspberry Pi Zero 2 W (obtainable through High Seas - got mine during Arcade)

(You will need to get your own speaker and AUX cable (LCSC has an AUX cable from UGREEN if you need it))

## API
If you do want to manupilate this for your own use...

### GET: /current
- Get the current song playing

```json
{
    "song_playing": "/Users/contyadvait/Music/contyshare/BoyWithUke - I Wish.mp3"
}
```

### GET: /super
- Organised version of songs, by artist

```json
{
"BoyWithUke": [
"Burn",
"I Wish",
"Animal Crackers",
"Falling for You",
"Pitfall",
"Paper Planes",
"Blurry Nights",
"Nightmare",
"Sick of U (feat. Oliver Tree)",
"Can You Feel It_",
"Let Me Down",
"Corduroy",
"IDGAF (feat. blackbear)",
"Lovely",
"Toxic",
"Long Drives",
"Understand",
"Petrichor (interlude)",
"Backseat",
"Ghost",
"Prairies (feat. mxmtoon)",
"Two Moons"
],
"Robotaki": [
"Dukkha",
"Butterscotch (feat. Jamie Fine & falcxne)",
"Obelisk",
"A Universal Truth",
"Los Angeles (feat. Maiah Manser)",
"Something from Nothing",
"Dreamcatcher (Night Mix) (feat. Miko)",
"Identity (feat. Record Heat)",
"Dreamcatcher (feat. Miko)-1",
"Holding On (feat. Billboard)",
"Now That We've Been in Love (feat. Pell)",
"Dreamcatcher (feat. Miko)",
"Quasar",
"Dreamcatcher (Night Mix)",
"Passing of Time",
"The Possibility of a Dream Coming True"
],
"Arctic Monkeys": [
"505",
"I Wanna Be Yours"
],
...
```

### GET: /available
- Every single available song (not organised)

```json
[
    "BoyWithUke - Burn",
    "Halden Rule & Aze - all for u",
    "BoyWithUke - I Wish",
    "Robotaki - Dukkha",
    "Robotaki - Butterscotch (feat. Jamie Fine & falcxne)",
    "Arctic Monkeys - 505",
    "Powfu & beabadoobee - death bed (coffee for your head)",
    "JVKE - lavender (feat. Pink Sweat$)",
    ...
]
```

### GET: /playlists
- Get all playlists configured by the user, with the songs it will play

```json
{
    "relax": [
        "BoyWithUke - I Wish.mp3",
        "BoyWithUke - Animal Crackers.mp3",
        "BoyWithUke - Nightmare.mp3",
        "BoyWithUke - Blurry Nights.mp3"
    ],
    "wind down": [
        "C418 - Minecraft.mp3",
        "C418 - Sweden.mp3",
        "C418 - Mice On Venus.mp3",
        "C418 - Subwoofer Lullaby.mp3",
        "C418 - Wet Hands.mp3",
        "C418 - Haggstrom.mp3"
    ]
}
```

### GET: /pause
- Pause the currently playing song

Success:
```json
{"message": "Paused playback"}
```

Error:
```json
{"error": "No song is currently playing"}
```

### GET: /resume
- Resume the paused song

Success:
```json
{"message": "Resumed playback"}
```

Error:
```json
{"error": "No song is currently paused"}
```

### GET: /stop
- Stop playback completely

Success:
```json
{"message": "Stopped playback"}
```

Error:
```json
{"error": "No song is currently playing"}
```

### POST: /play
- Accepts a JSON of what is to be played

Example input (playlist):
```json
{
    "key": "somepassword",
    "playlist": "relax"
}
```

Example input (song):
```json
{
    "key": "somepassword",
    "song": "BoyWithUke - Burn"
}
```

### POST: /play-with-mood
- Accepts a JSON with a custom Mood or Vibe to play and plays a song through AI

Example input
```json
{
    "key": "somepassword",
    "mood": "happy"
}
```