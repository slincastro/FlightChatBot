import spacy
import unicodedata
import extractors.date_extractor as date_extractor
import extractors.airline_extractor as airline_extractor
import extractors.location_extractor as location_extractor
import extractors.ticket_extractor as ticket_extractor
import extractors.airport_extractor as airport_extractor
import domain.reserve as reserve
from driven_adapters.airport_client import AirportClient
from googletrans import Translator
import flight_speaker as fs
import flight_listener as fl
import flight_matcher as fm

nlp = spacy.load("es_core_news_sm")
is_talked = False
is_call_printed = True
is_log_printed = True

def print_call(request):
    if is_call_printed:
        print(request)
        return

def print_log(request):
    if is_log_printed:
        print(request)
        return

def quitar_acentos(texto):
    texto_normalizado = unicodedata.normalize('NFD', texto)
    
    return ''.join([c for c in texto_normalizado if not unicodedata.combining(c)])

def get_airports(text):
    #TODO: get api_key and api_secret from environment variables
    api_key = '098aad84c5'
    api_secret ='c12d1f455daa01a'
   # api_key = '3ef88b63e1'
   # api_secret = 'e406df83ea63f72'

    informacion_aeropuertos, airports_number = AirportClient(api_key, api_secret).get_airport_values(text)

    if airports_number == 0:
        return None
    
    return informacion_aeropuertos

def get_airports_by(city):
    translated_city = Translator().translate(city, src='es', dest='en')
        
    airports = get_airports(translated_city.text)
    
    return airports

def search_airports(request_llamada):
    individual_extractors = [
        reserve.Reserve("origen", location_extractor.LocationExtractor(request_llamada).extract_origen, "Cual es la ciudad de partida de su vuelo ?"),
        reserve.Reserve("destino", location_extractor.LocationExtractor(request_llamada).extract_destino,   "Cual es la ciudad de destino de su vuelo ?")
    ]
    
    iata_codes = {"origen": "IATA_FROM", "destino": "IATA_TO"}
    has_valid_airport = False

    while not has_valid_airport:
        for extractor in individual_extractors:
            
            translated_city = Translator().translate(quitar_acentos(request_llamada[extractor.nombre]), src='es', dest='en')
            
            print_log(f"ciudad traducida {translated_city.text}")
            airports = get_airports(translated_city.text)

            airports_in_city = [airport for airport in airports if airport["city"].lower() == translated_city.text.lower()]
            
            if airports_in_city is None and len(airports_in_city) == 0:
                speak("Disculpa no encontramos un aeropuerto para tu vuelo , podrias decidir otra ciudad "+ extractor.nombre)
                user_input = listen()
                selected_city = extractor.extractor(user_input)
                request_llamada[extractor.nombre] = selected_city
                print_log(selected_city)
                print_call(request_llamada)

                has_valid_airport = False
                break
            
            elif len(airports) > 3 and len(airports_in_city) == 0:
                speak(f"Disculpa al parecer seleccionaste un pais de {extractor.nombre} obtuvimos {len(airports)} aeropuertos, podrias decidir una ciudad de "+ extractor.nombre)
                user_input = listen()
                selected_city = extractor.extractor(user_input)
                print_log(selected_city)
                print_call(request_llamada)
                request_llamada[extractor.nombre] = selected_city
                
                has_valid_airport = False
                break
                
            elif len(airports_in_city) == 1:
                request_llamada[iata_codes[extractor.nombre]] = airports[0]["iata"]
                has_valid_airport = True
                
            else:
                airports_codes = []
                speak("Disculpa encontramos mas de un aeropuerto para tu vuelo " + extractor.nombre + ", podrias decidir entre los siguientes, para decidir recuerda el numero del aeropuerto :")
                count = 1
                
                for airport in airports_in_city:
                    airport_code = {}
                    airport_code["name"] = airport["name"]
                    airport_code["number"] = count
                    airport_code["iata"] = airport["iata"]
                    
                    airports_codes.append(airport_code)
                    speak(str(count) + " " + airport["name"])
                    
                    count += 1
                    
                texto_aeropuerto = listen()
                numero_aeropuerto = airport_extractor.AirportExtractor(None).specific_extraction(texto_aeropuerto) 
                
                if numero_aeropuerto is None:
                    speak("Disculpa no entendi, podrias repetir el numero del aeropuerto")
                    user_input = input("Tú: ")
                    airport_extractor.AirportExtractor(None).specific_extraction(user_input)
                    print(request_llamada)
                    
                numero_aeropuerto = int(numero_aeropuerto)
              #  print(airports_codes[numero_aeropuerto - 1])
                request_llamada[iata_codes[extractor.nombre]] = airports_codes[numero_aeropuerto - 1]["iata"]
                has_valid_airport = True

def listen():
    if not is_talked:
       user_input = input("Tú: ")
       return user_input
          
    user_input = fl.FlightListener().listen()
    return user_input.lower()
    
def speak(mensaje):
    if is_talked:
        fs.FlightSpeaker().speak(mensaje)

    print("="*30)
    print("Chatbot:", mensaje)


def process_retry(extractor, request_llamada, mensaje):
    speak(mensaje)
    user_input = listen()
    extractor.extractor(user_input)
    print_call(request_llamada)  
    
def is_complete(request_llamada):
    none_found = False
    for key, value in request_llamada.items():
        if value is None:
            none_found = True
            
    return not none_found

def validate(request_llamada):
    individual_extractors = [
        reserve.Reserve("aerolinea", airline_extractor.AirlineExtractor(request_llamada).extract, "En que Aerolinea te gustaria viajar ?"),
        reserve.Reserve("fecha", date_extractor.DateExtractor(request_llamada).extract, "En que fecha te gustaria viajar ?"),
        reserve.Reserve("origen", location_extractor.LocationExtractor(request_llamada).extract_origen, "Desde donde saldria tu vuelo ?"),
        reserve.Reserve("destino", location_extractor.LocationExtractor(request_llamada).extract_destino,   "Hacia que ciudad viajas ?"),
        reserve.Reserve("cantidad", ticket_extractor.TicketExtractor(request_llamada).specific_extraction, "Cuantos boletos desea reservar ?")
    ]
    
    for extractor in individual_extractors:
        if request_llamada[extractor.nombre] == None :
            process_retry(extractor, request_llamada, extractor.question)
            times = 0
            
            while request_llamada[extractor.nombre] == None:
                if times == 3:
                    speak("Disculpa No entendi, podrias escribir "+ extractor.question)
                    user_input = input("Tú: ")
                    extractor.extractor(user_input)
                    print_call(request_llamada)
                    times = 0
                    
                message = "Disculpa No entendi, puedes repetir "+ extractor.question
                process_retry(extractor, request_llamada, message)
                times += 1      
            

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
        
    print_call(llamada)
    
    while not is_complete(llamada):
        validate(llamada)
    
    search_airports(llamada)
    
    speak("Queremos confirmar los datos de su vuelo :")
    speak("Quieres comprar " + str(llamada["cantidad"]) + " boletos, para el " + llamada["fecha"] + ", por la aerolina " + llamada["aerolinea"] + ", partiendo de " + llamada["origen"] + ", hacia " + llamada["destino"])
    speak("Es correcto ?")                
                       
    print(llamada)
    
    return "Vamos a reservar tu vuelo."
 