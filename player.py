import threading
import sounddevice as sd
import soundfile as sf
import numpy as np

class MusicPlayer:
    def __init__(self):
        self.stream = None
        self.song_playing = ""
        self.is_playing = False
        self.lock = threading.Lock()
        self.data = None
        self.samplerate = None
        self.position = 0
        self.playlist_thread = None

    def callback(self, outdata, frames, time, status):
        if self.position < len(self.data):
            chunk = self.data[self.position:self.position + frames]
            if len(chunk) < frames:
                outdata[:len(chunk)] = chunk
                outdata[len(chunk):] = np.zeros((frames - len(chunk), 2))
                raise sd.CallbackStop()
            else:
                outdata[:] = chunk
            self.position += frames
        else:
            raise sd.CallbackStop()

    def play(self, song_path):
        with self.lock:
            if self.is_playing:
                self.stop()

            try:
                self.data, self.samplerate = sf.read(song_path)
                if len(self.data.shape) == 1:
                    self.data = np.column_stack((self.data, self.data))

                self.position = 0
                self.stream = sd.OutputStream(
                    samplerate=self.samplerate,
                    channels=2,
                    callback=self.callback
                )
                self.stream.start()
                self.is_playing = True
                self.song_playing = song_path
                return True
            except Exception as e:
                print(f"Error playing file: {e}")
                return False

    def play_playlist(self, playlist):
        def playlist_worker():
            for song in playlist:
                if not self.play(song):
                    print(f"Failed to play: {song}")
                while self.is_playing:
                    continue  # Wait for the current song to finish before proceeding

        self.playlist_thread = threading.Thread(target=playlist_worker)
        self.playlist_thread.start()

    def pause(self):
        with self.lock:
            if self.is_playing and self.stream:
                self.stream.stop()
                return True
            return False

    def resume(self):
        with self.lock:
            if self.is_playing and self.stream:
                self.stream.start()
                return True
            return False

    def stop(self):
        with self.lock:
            if self.stream:
                self.stream.stop()
                self.stream.close()
                self.stream = None
                self.is_playing = False
                self.song_playing = ""
                self.data = None
                self.position = 0
                return True
            return False