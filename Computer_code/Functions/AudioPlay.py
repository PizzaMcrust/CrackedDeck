import pyaudio
from pygame import mixer
import time

def playsound(file_path):
    p = pyaudio.PyAudio()
    print("Playback devices:")
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        if info['maxOutputChannels'] > 0:
            print(f"Index {i}: {info['name']}")
    p.terminate()

    target_device_index = 'CABLE Input (VB-Audio Virtual Cable)'

    mixer.pre_init(devicename=target_device_index)
    mixer.init()
    print(f"Using output device: {mixer.get_init()}")
    mixer.music.load(file_path)
    mixer.music.play()

    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(0.1)
    
    mixer.quit()