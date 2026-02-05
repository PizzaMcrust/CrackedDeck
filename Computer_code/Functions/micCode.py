import pyaudio

RATE = 8000      # telephone quality
CHUNK = 256

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paUInt8,
                channels=1,
                rate=RATE,
                output=True)

audio_buffer = bytearray()

def audioRead():
    pass