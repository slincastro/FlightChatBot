import spacy
from spacy.matcher import Matcher
import extractors.date_extractor as date_extractor
import extractors.airline_extractor as airline_extractor
import extractors.location_extractor as location_extractor
import extractors.ticket_extractor as ticket_extractor
import extractors.domain.reserve as reserve
import flight_speaker as fs
import flight_listener as fl
import flight_matcher as fm
import time

nlp = spacy.load("es_core_news_sm")

def listen():
    user_input = fl.FlightListener().listen()
    return user_input.lower()
    #input("Tú: ")

def speak(mensaje):
    fs.FlightSpeaker().speak(mensaje)
    print("Chatbot:", mensaje)
    
def is_complete(request_llamada):

    none_found = False
    for key, value in request_llamada.items():
        if value is None:
            none_found = True
            
    return not none_found

def validate(request_llamada):
    if request_llamada["aerolinea"] == None :
        speak("Cual es la aerolinea de su vuelo ?")
        user_input = listen()
        aerolinea = airline_extractor.AirlineExtractor(request_llamada).extract(user_input)
        request_llamada["aerolinea"] = aerolinea
        print(request_llamada)
    
    if request_llamada["fecha"] == None :
        speak("Cual es la fecha de su vuelo ?")
        user_input = listen()
        fecha = date_extractor.DateExtractor(request_llamada).extract(user_input)
        request_llamada["fecha"] = fecha
        print(request_llamada)
        
    if request_llamada["origen"] == None :
        speak("Cual es la ciudad de partida de su vuelo ?")
        user_input = listen()
        origen, destino = location_extractor.LocationExtractor(request_llamada).extract(user_input)
        request_llamada["origen"] = origen
        print(request_llamada)
        
    if request_llamada["destino"] == None :
        speak("Cual es la ciudad de destino de su vuelo ?")
        user_input = listen()
        origen, destino = location_extractor.LocationExtractor(request_llamada).extract(user_input)
        request_llamada["destino"] = destino
        print(request_llamada)
        
    if request_llamada["cantidad"] == None :
        speak("Cuantos boletos desea reservar ?")
        user_input = listen()
        cantidad = ticket_extractor.TicketExtractor(request_llamada).extract(user_input)
        request_llamada["cantidad"] = cantidad
        print(request_llamada)
        
    return request_llamada

def process_input(user_input):
    
    llamada = {
        "origen":"",
        "destino":"",
        "fecha":"",
        "cantidad":"",
        "aerolinea":""
    }
    
    extractors = [reserve.Reserve("Aerolinea", airline_extractor.AirlineExtractor(llamada)),
                  reserve.Reserve("Fecha", date_extractor.DateExtractor(llamada)),
                  reserve.Reserve("Origen", location_extractor.LocationExtractor(llamada)),
                  reserve.Reserve("cantidad", ticket_extractor.TicketExtractor(llamada)),    
                  ] 
    
    for flight_extractor in extractors:
        flight_extractor.extractor.extract(user_input)
        
    print(llamada)
    
    while not is_complete(llamada):
        validate(llamada)
    
    print(llamada)
    
    return "Vamos a reservar tu vuelo."
 

while True:
    mensaje = "Hola, bienvenido a sky tu travel, en que te puedo ayudar?"
    print("Hola, bienvenido a sky2travel, en que te puedo ayudar?")
    fs.FlightSpeaker().speak(mensaje)

    user_input = listen()
    #user_input = input("Tú: ")
    if user_input.lower() == "salir":
        break
    
    response = process_input(user_input)
    print("Chatbot:", response)
