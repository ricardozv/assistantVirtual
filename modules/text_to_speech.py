from gtts import gTTS
import os

def text_to_speech(text):
    tts = gTTS(text=text, lang='pt')
    tts.save("output.mp3")
    os.system("start output.mp3")
