import nlp_engine as nlpe
import flight_speaker as fs

user_input = ""
is_talked = False

while user_input.lower() not in ["si", "no"]:    
    print("Hola, quieres usar el chatbot por voz ?(si/no)")
    user_input = input("Tú: ")
    is_talked = user_input.lower() == "si"
    nlpe.set_if_is_talked(is_talked)


mensaje = "Hola, bienvenido a sky tu travel, en que te puedo ayudar?"
print("Hola, bienvenido a sky2travel, en que te puedo ayudar?")

if is_talked:
    fs.FlightSpeaker().speak(mensaje)
    user_input = nlpe.listen()
else:
    user_input = input("Tú: ")


response = nlpe.process_input(user_input)

print("Chatbot:", response)