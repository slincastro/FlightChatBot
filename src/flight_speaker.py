from gtts import gTTS
import pyttsx3
import os

class FlightSpeaker:
    
    def speak(self, text):
        sistema_operativo = os.name

        if sistema_operativo == 'nt':
            self.speak_windows(text)
        elif sistema_operativo == 'posix':
            self.speak_mac(text)
            
    def speak_mac(self, text):
        tts = gTTS(text=text, lang='es')
        tts.save("./audios/voz.mp3")
        os.system("afplay ./audios/voz.mp3")
        
    def speak_windows(self, text):
        engine = pyttsx3.init(driverName='sapi5')
        engine.setProperty('voice', 'spanish-latam')
        engine.say(text)
        engine.runAndWait()
        

