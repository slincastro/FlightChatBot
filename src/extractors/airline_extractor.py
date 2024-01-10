import spacy

class AirlineExtractor:
    def __init__(self, llamada_reserva):
        self.modelo = spacy.load("./airline-model")
        self.llamada_reserva = llamada_reserva

    def extract(self, text):
        doc = self.modelo(text)
        aerolinea = [ent.text for ent in doc.ents]
        self.llamada_reserva["aerolinea"]= aerolinea[0] if aerolinea is not None and len(aerolinea) > 0 else None
        return aerolinea

        

