import spacy

class LocationExtractor:
    def __init__(self):
        self.nlp = spacy.load("es_core_news_sm")

    def extract(self, text):
        doc = self.nlp(text)
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

        return origen, destino