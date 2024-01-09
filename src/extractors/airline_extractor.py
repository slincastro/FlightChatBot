import spacy

class AirlineExtractor:
    def __init__(self):
        self.modelo = spacy.load("./airline-model")

    def extract(self, text):
        doc = self.modelo(text)
        return [ent.text for ent in doc.ents]
# Texto de prueba
#texto_prueba = "quiero viajar el 2 de febrero de madrid a santiago en Lufthansa"

# Procesar el texto con el modelo entrenado
#doc = modelo_entrenado(texto_prueba)
#print(doc)
# Imprimir las entidades encontradas
#print("Entidades encontradas:", [(ent.text, ent.label_) for ent in doc.ents])
