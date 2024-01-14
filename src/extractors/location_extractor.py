import spacy

class LocationExtractor:
    def __init__(self, llamada_reserva):
        self.nlp = spacy.load("es_core_news_sm")
        self.llamada_reserva = llamada_reserva

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

        self.llamada_reserva["origen"] = origen
        self.llamada_reserva["destino"] = destino
        
        return origen, destino
    
    def extract_origen(self, text):
        doc = self.nlp(text)
        ubicaciones = [ent for ent in doc.ents if ent.label_ == "LOC"]
        preposiciones_origen = ["de", "desde", "partiendo de", "saliendo de", ""]
        origen = None

        for ubicacion in ubicaciones:
            if hasattr(doc, 'tokens'):
                if doc.tokens == 1: 
                    origen = ubicacion.text
                    break
            preposicion = doc[ubicacion.start - 1].text.lower() if ubicacion.start > 0 else ''
            if preposicion in preposiciones_origen:
                origen = ubicacion.text
                
        self.llamada_reserva["origen"] = origen
        return origen
    
    def extract_destino(self, text):
        doc = self.nlp(text)
        ubicaciones = [ent for ent in doc.ents if ent.label_ == "LOC"]
        preposiciones_destino = ["a", "hasta", "hacia", "para", ""]
        destino = None

        for ubicacion in ubicaciones:
            if hasattr(doc, 'tokens'):
                if doc.tokens == 1: 
                    destino = ubicacion.text
                    break
            preposicion = doc[ubicacion.start - 1].text.lower() if ubicacion.start > 0 else ''
            if preposicion in preposiciones_destino:
                destino = ubicacion.text
        self.llamada_reserva["destino"] = destino
        
        return destino