import spacy
from spacy.matcher import Matcher
import extractors.date_extractor as date_extractor
import extractors.airline_extractor as airline_extractor
import extractors.location_extractor as location_extractor
import extractors.ticket_extractor as ticket_extractor

import flight_matcher as fm
nlp = spacy.load("es_core_news_sm")


def process_input(user_input):
    
    llamada = {
        "origen":"",
        "destino":"",
        "fecha":"",
        "cantidad":"",
        "aerolinea":""
    }
    
    doc = nlp(user_input)
    
    aerolinea = airline_extractor.AirlineExtractor().extract(user_input)
    fecha = date_extractor.DateExtractor().extract(user_input)
    origen, destino = location_extractor.LocationExtractor().extract(user_input)
    cantidad = ticket_extractor.TicketExtractor().extract(user_input)
    
    llamada["aerolinea"]=aerolinea[0]
    llamada["fecha"]=fecha[0]  
    llamada["origen"] = origen
    llamada["destino"] = destino
    llamada["cantidad"] = cantidad
        
    print(llamada)
    
    return handle_reservar_vuelo(doc)

def handle_reservar_vuelo(doc):
    return "Vamos a reservar tu vuelo."


while True:
    user_input = input("Tú: ")
    if user_input.lower() == "salir":
        break
    response = process_input(user_input)
    print("Chatbot:", response)
