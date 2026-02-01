import pyaudio
from pygame import mixer
from pydub import AudioSegment
from pydub.playback import play
import time
import io

def playsound(file_path, target_device_name="CABLE Input (VB-Audio Virtual Cable)"):
    
    # #Find and set the target output device
    # p = pyaudio.PyAudio()
    # print("Playback devices:")
    # for i in range(p.get_device_count()):
    #     info = p.get_device_info_by_index(i)
    #     if info['maxOutputChannels'] > 0:
    #         print(f"Index {i}: {info['name']}")
    # p.terminate()

    # target_device_index = 'CABLE Input (VB-Audio Virtual Cable)'
    # mixer.pre_init(devicename=target_device_index)

    # #Load and play the audio file

    # Audio = AudioSegment.from_file(file_path)  

    # wav_io = io.BytesIO()
    # Audio.export(wav_io, format="wav")
    # wav_io.seek(0)

    # print(wav_io)
    # mixer.init()
    # mixer.music.load(wav_io)
    # mixer.music.play()

    # while mixer.music.get_busy():  # wait for music to finish playing
    #     time.sleep(0.1)
    
    # mixer.quit()

    # Step 1: List playback devices and find target index
    p = pyaudio.PyAudio()
    print("Playback devices:")
    target_index = None
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        if info['maxOutputChannels'] > 0:
            print(f"Index {i}: {info['name']}")
            if target_device_name in info['name']:
                target_index = i
                print(f"Found target: Index {i}")
    
    if target_index is None:
        print("Target device not found! Using default.")
        target_index = None  # Default device
    
    # Step 2: Load MP3 and convert to raw PCM
    audio = AudioSegment.from_mp3(file_path)
    TARGET_RATE = 48000
    audio = audio.set_channels(2).set_sample_width(2)  # Standardize
    raw_data = audio.raw_data  # PCM bytes
    
    # Step 3: Open stream on specific device
    stream = p.open(
        format=pyaudio.paInt16,
        channels=audio.channels,
        rate=TARGET_RATE,
        output=True,
        output_device_index=target_index,
        frames_per_buffer=1024  # CHUNK size
    )
    
    # Step 4: Play in chunks
    CHUNK = 1024
    for i in range(0, len(raw_data), CHUNK * audio.channels * 2):
        chunk = raw_data[i:i + CHUNK * audio.channels * 2]
        stream.write(chunk)
    
    # Step 5: Cleanup
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("Playback finished!")

#playsound(r"C:\Users\stand\Documents\Programs\Cracked-deck\Media\BUZZ.mp3")  # Test call (remove or comment out in production)