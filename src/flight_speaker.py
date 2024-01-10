from gtts import gTTS
import os

class FlightSpeaker:
    def speak(self, text):
        tts = gTTS(text=text, lang='es')
        tts.save("./audios/voz.mp3")
        os.system("afplay ./audios/voz.mp3")

