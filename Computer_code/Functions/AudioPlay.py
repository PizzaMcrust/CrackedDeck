import pyaudio

Audio = pyaudio.PyAudio()

def play_sound(file_path):
    Audio.open()