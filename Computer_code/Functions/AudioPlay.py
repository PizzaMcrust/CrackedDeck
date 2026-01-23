import pyaudio
from pygame import mixer
from pydub import AudioSegment
from pydub.playback import play
import time
import io

def playsound(file_path):
    
    #Find and set the target output device
    p = pyaudio.PyAudio()
    print("Playback devices:")
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        if info['maxOutputChannels'] > 0:
            print(f"Index {i}: {info['name']}")
    p.terminate()

    target_device_index = 'CABLE Input (VB-Audio Virtual Cable)'
    mixer.pre_init(devicename=target_device_index)

    #Load and play the audio file

    Audio = AudioSegment.from_file(file_path)  

    wav_io = io.BytesIO()
    Audio.export(wav_io, format="wav")
    wav_io.seek(0)

    print(wav_io)
    mixer.init()
    mixer.music.load(wav_io)
    mixer.music.play()

    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(0.1)
    
    mixer.quit()

#playsound(r"C:\Users\stand\Documents\Programs\Cracked-deck\Media\BUZZ.mp3")  # Test call (remove or comment out in production)