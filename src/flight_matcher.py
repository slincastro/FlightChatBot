import spacy
from spacy.matcher import Matcher

class FlightMatcher:
    def __init__(self, nlp):
        self.nlp = nlp

    def get_matcher(self):
        matcher = Matcher(self.nlp.vocab)
        pattern_reservar = [{"LOWER": "reservar"}, {"LOWER": "vuelo"}]
        pattern_cancelar = [{"LOWER": "cancelar"}, {"LOWER": "reserva"}]
        matcher.add("RESERVAR_VUELO", [pattern_reservar])
        matcher.add("CANCELAR_RESERVA", [pattern_cancelar])
        
        return matcher