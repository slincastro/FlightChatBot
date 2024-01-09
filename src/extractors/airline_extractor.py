import spacy

class AirlineExtractor:
    def __init__(self):
        self.modelo = spacy.load("./airline-model")

    def extract(self, text):
        doc = self.modelo(text)
        return [ent.text for ent in doc.ents]

