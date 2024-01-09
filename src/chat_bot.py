import spacy
from spacy.matcher import Matcher
import extractors.date_extractor as date_extractor
import extractors.airline_extractor as airline_extractor

import flight_matcher as fm
nlp = spacy.load("es_core_news_sm")


def extract_locations(doc):

    ubicaciones = [ent for ent in doc.ents if ent.label_ == "LOC"]
    preposiciones_origen = ["de", "desde", "partiendo de", "saliendo de"]
    preposiciones_destino = ["a", "hasta", "hacia", "para"]

    origen, destino = None, None


    for ubicacion in ubicaciones:

        preposicion = doc[ubicacion.start - 1].text.lower() if ubicacion.start > 0 else ''
    
        if preposicion in preposiciones_origen:
            origen = ubicacion.text
        elif preposicion in preposiciones_destino:
            destino = ubicacion.text

    print(f"Origen: {origen}, Destino: {destino}")
    return origen, destino

def extract_ticket_number(doc):
    # Inicializar la variable para el número de boletos
    num_boletos = None

    # Buscar entidades numéricas seguidas por la palabra "boletos"
    for token in doc:
        if token.text.lower() in ["boleto","boletos" ,"ticket" ,"tickets" ,'pasaje' , 'pasajes','asiento' ,'asientos', 'vuelo', 'vuelos']:
            # Verificar si el token anterior es un número
            index = token.i - 1
            if doc[index].is_digit:
                num_boletos = int(doc[index].text)
                break

    print(f"Número de boletos: {num_boletos}")
    return num_boletos

def process_input(user_input):
    
    llamada = {
        "origen":"",
        "destino":"",
        "fecha":"",
        "cantidad":"",
        "aerolinea":""
    }
    
    aerolinea = airline_extractor.AirlineExtractor().extract(user_input)
    
    llamada["aerolinea"]=aerolinea[0]
    doc = nlp(user_input)
    
    fecha = date_extractor.ExtractorFechas().extraer_fechas(user_input)
    
    llamada["fecha"]=fecha[0]
    
    origen, destino = extract_locations(doc)
    llamada["origen"] = origen
    llamada["destino"] = destino
    
    cantidad = extract_ticket_number(doc)
    llamada["cantidad"] = cantidad
    
    extract_ticket_number(doc)
       
    stop_words_modificadas = nlp.Defaults.stop_words - {"de", "a", "desde", "hasta", "hacia"}

    tokens_limpios = [token.text.lower() for token in doc if not token.is_punct]
    print("="*30)
    print(tokens_limpios)


    tokens_sin_stopwords = [token.text.lower() for token in doc if token.text.lower() not in stop_words_modificadas]

    print(tokens_sin_stopwords)
    
    for ent in doc.ents:
        print(f"{ent.text} - {ent.label_}")
        
    print(llamada)
    
    
    return handle_reservar_vuelo(doc)

# Funciones para manejar intenciones específicas
def handle_reservar_vuelo(doc):
    return "Vamos a reservar tu vuelo."

def handle_cancelar_reserva(doc):
    return "Tu reserva ha sido cancelada."


while True:
    user_input = input("Tú: ")
    if user_input.lower() == "salir":
        break
    response = process_input(user_input)
    print("Chatbot:", response)
