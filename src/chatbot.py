import nlp_engine as nlpe
import flight_speaker as fs

user_input = ""

while user_input.lower() not in ["si", "no"]:    
    print("Hola, quieres usar el chatbot por voz ?(si/no)")
    user_input = input("Tú: ")
    is_talked = user_input.lower() == "si"


mensaje = "Hola, bienvenido a sky tu travel, en que te puedo ayudar?"
print("Hola, bienvenido a sky2travel, en que te puedo ayudar?")
if is_talked:
    fs.FlightSpeaker().speak(mensaje)
    user_input = nlpe.listen()
else:
    #user_input = "quiero 3 vuelos para viajar de Ecuador a quito el 4 de marzo por avianca"
    user_input = input("Tú: ")
#user_input = input("Tú: ")
#if user_input.lower() == "salir":
    #break

response = nlpe.process_input(user_input)

print("Chatbot:", response)