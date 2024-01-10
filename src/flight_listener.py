import speech_recognition as sr

class FlightListener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self):
        with self.microphone as source:
            audio = self.recognizer.listen(source)
            
        try:
            texto = self.recognizer.recognize_google(audio, language="es-ES")
            print("Creo que dijiste: " + texto)
            return texto
        except sr.UnknownValueError:
            print("No entendí lo que dijiste.")
        except sr.RequestError as e:
            print(f"Error en el servicio de Google; {e}")
            
        return ""
