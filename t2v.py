from gtts import gTTS
import os
def speechTrans(data):
    speech = gTTS(data)
    speech.save("hello1.mp3")
    os.system("start hello1.mp3")