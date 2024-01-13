import spacy
from spacy.training import Example
import random

TRAIN_DATA = []

numeros = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve","diez","once"]

oraciones_base = [
    "quiero {} tickets",
    "quiero {} boletos",
    "quiero {}",
    "quiero {} asientos",
    "hola, quiero {} asientos para mi viaje",
    "hola, quiero {} boletos para mi viaje",
    "hola, quiero {} para mi viaje",
    "hola, quiero {} tickets para mi viaje",
    "necesito {} tickets",
    "necesito {} boletos",
    "necesito {}",
    "necesito {} asientos",
    "me gustarian {} tickets",
    "me gustarian {} boletos",
    "me gustarian {}",
    "me gustarian {} asientos",
    "son {} tickets",
    "son {} boletos",
    "son {}",
    "son {} asientos",
    "{} tickets",
    "{} boletos",
    "{}",
    "{}",
    "{}",
    "{}",
    "{}",
    "{}",
    "{} asientos",
    "quiero reservar {} tickets",
    "quiero reservar {} boletos",
    "quiero reservar {}",
    "quiero reservar {} asientos",
    "necesito comprar {} tickets",
    "necesito comprar {} boletos",
    "necesito comprar {}",
    "necesito comprar {} asientos",
]

for _ in range(500):  
    aerolinea = random.choice(numeros)
    aerolinea = aerolinea.lower()
    oracion = random.choice(oraciones_base).format(aerolinea)
    inicio = oracion.find(aerolinea)
    fin = inicio + len(aerolinea)
    TRAIN_DATA.append((oracion, {"entities": [(inicio, fin, "TICKETS")]}))

print(f"Entrenando con {len(TRAIN_DATA)} combinaciones")

nlp = spacy.load("es_core_news_sm")
if "ner" not in nlp.pipe_names:
    ner = nlp.create_pipe("ner")
    nlp.add_pipe("ner", last=True)
else:
    ner = nlp.get_pipe("ner")

ner.add_label("NUMEROTICKETS")

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

nlp.to_disk("./ticket-model")
