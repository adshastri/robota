import pyaudio
import wave
import requests
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNOperationType, PNStatusCategory

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100 
CHUNK = 1028
RECORD_SECONDS = 4
WAVE_OUTPUT_FILENAME = "file.wav"
  
audio = pyaudio.PyAudio()
   
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                           rate=RATE, input=True,
                                           frames_per_buffer=CHUNK)
print ("recording...")
frames = []
    
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print ("finished recording")
    # stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
                   
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

data = open('./file.wav', 'rb').read()
r = requests.post("https://stream.watsonplatform.net/speech-to-text/api/v1/recognize", auth=("aca70723-d062-4e51-8993-31c8724eb644", "UGwnIEOZpTzv"), headers={"Content-Type": "audio/wav", }, data=data);
print (r.json()['results'][0]['alternatives'][0]['transcript']);

transcript = r.json()['results'][0]['alternatives'][0]['transcript'];


pnconfig = PNConfiguration()
pnconfig.publish_key = "pub-c-1f2b2cf3-7bd3-4ab4-a8d1-cb673e49572e"
pnconfig.subscribe_key = "sub-c-46613428-381c-11e7-ae4f-02ee2ddab7fe"
pnconfig.ssl = False
  
pubnub = PubNub(pnconfig)

def publish_callback(result, status):
    print (status);
    print (result);

pubnub.publish().channel("sentiment_analyzer").message(transcript).async(publish_callback);
