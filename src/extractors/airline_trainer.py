import spacy
from spacy.training import Example
import random

TRAIN_DATA = []

nombres_aerolineas = ["Lufthansa", "Iberia", "Ryanair", "Emirates", "Delta", "American Airlines", "United", "Air France", "British Airways", "Qantas"]
aerolineas_sudamericanas = ["LATAM Airlines", "Aerolíneas Argentinas", "Avianca", "Copa Airlines", "GOL Linhas Aéreas", "Azul Linhas Aéreas", "Sky Airline", "TAM Airlines", "Peruvian Airlines", "Aeromar", "Aeroregional", "Viva Air", "Amaszonas", "Andes Líneas Aéreas", "Star Peru", "LCPerú", "EasyFly", "Flybondi", "JetSmart", "Flycana", "Flyest", "Fly Sur", "Plus Ultra Líneas Aéreas"]

nombres_aerolineas = nombres_aerolineas + aerolineas_sudamericanas

oraciones_base = [
    "Vuelo con {}",
    "Mi vuelo es con {}",
    "Reservé un billete en {}",
    "Prefiero viajar con {}",
    "He elegido {} para mi viaje",
    "Estoy volando con {}",
    "Mi reserva es con {}",
    "Elegí {} para mi vuelo",
    "Voy a viajar con {}",
    "Estoy considerando volar con {}",
    "quiero viajar el 2 de febrero de Madrid a Santiago en {}",
    "quiero viajar en {} el 4 de marzo de Quito a Guayaquil",
    "necesito 3 voletos para viajar en {} de paris a londres",
    "quiero viajar el 2 de febrero de Madrid a Santiago en {}.",
    "quiero viajar en {} el 4 de marzo de Quito a Guayaquil.",
    "necesito 3 boletos para viajar en {} de París a Londres.",
    "Me gustaría reservar un vuelo en {} el 10 de abril desde Nueva York a Los Ángeles.",
    "Necesito comprar un billete para viajar el 5 de junio de Madrid a Barcelona. por {}",
    "Quiero hacer una reserva para el vuelo de {} a Miami el 15 de mayo.",
    "¿Tienes disponibilidad para vuelos en {} el 8 de agosto desde Roma a Atenas?",
    "Necesito encontrar un vuelo de Okinawa a Tokio para el 12 de septiembre. en {}",
    "Estoy buscando boletos para volar el 25 de octubre de Mendoza a Buenos Aires en {}.",
    "¿Puedes proporcionarme información sobre vuelos en {} desde Pune a Nueva Delhi el 30 de noviembre?",
    "Estoy planeando un viaje el 20 de julio desde Monterrey a Cancún en {}, ¿puedes ayudarme?",
    "Quiero reservar un vuelo en {} de Madrid a Nueva York para el 18 de diciembre.",
    "Necesito comprar boletos para viajar en {} el 7 de enero de Ciudad de México a Bogotá.",
    "¿Cuál es el precio de los vuelos de {} a San Francisco el 22 de marzo?",
    "Estoy interesado en volar en {} el 14 de mayo a Los Ángeles.",
    "¿Tienes ofertas de vuelos desde Buerdeos a París en {} para el 3 de septiembre?",
    "Quiero reservar un vuelo de ida y vuelta desde Manchester a Londres del 9 al 16 de octubre por {}.",
    "Necesito tres boletos para el vuelo de {} a Barcelona el 11 de noviembre.",
    "¿Cuál es el horario de vuelos de {} a Miami el 6 de febrero?",
    "Me gustaría encontrar un vuelo en {} para el 13 de abril a Las Vegas.",
    "¿Puedes ayudarme a encontrar vuelos desde Pekin a Tokio el 19 de julio usando {} ?",
    "Estoy buscando un vuelo de {} a Río de Janeiro el 21 de agosto.",
    "Necesito boletos para un viaje en {} a Sydney el 27 de diciembre.",
    "¿Cuáles son las opciones de vuelos desde Miami a Toronto el 9 de marzo en {} ?",
    "Quiero reservar un vuelo en {} el 15 de octubre a Cancún.",
    "Estoy interesado en vuelos desde Galapagos a Madrid el 28 de septiembre, en {}.",
    "¿Puedes proporcionarme información sobre vuelos en {} desde Sidney a Bangkok el 2 de noviembre?",
    "Necesito comprar boletos para volar en {} el 16 de enero a Ciudad de México.",
    "¿Cuál es el costo de los vuelos desde Astana a Los Ángeles el 12 de julio por {}?",
    "Quiero reservar un vuelo en {} de Lima a Buenos Aires para el 4 de mayo.",
    "¿Tienes disponibilidad para vuelos desde Berlin a Barcelona el 23 de febrero en {}?"
]

for _ in range(1000):  
    aerolinea = random.choice(nombres_aerolineas)
    oracion = random.choice(oraciones_base).format(aerolinea)
    inicio = oracion.find(aerolinea)
    fin = inicio + len(aerolinea)
    TRAIN_DATA.append((oracion, {"entities": [(inicio, fin, "AEROLINEA")]}))

print(f"Entrenando con {len(TRAIN_DATA)} combinaciones")

nlp = spacy.load("es_core_news_sm")
if "ner" not in nlp.pipe_names:
    ner = nlp.create_pipe("ner")
    nlp.add_pipe("ner", last=True)
else:
    ner = nlp.get_pipe("ner")

ner.add_label("AEROLINEA")

other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]

with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.begin_training()
    for itn in range(10): 
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in TRAIN_DATA:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            nlp.update([example], drop=0.5, sgd=optimizer, losses=losses)
        print(losses)

nlp.to_disk("./airline-model")
