import spacy

class TicketExtractor:
    def __init__(self):
        self.nlp = spacy.load("es_core_news_sm")
    
    def extract(self, text):
        num_boletos = None
        doc = self.nlp(text)
        for token in doc:
            if token.text.lower() in ["boleto","boletos" ,"ticket" ,"tickets" ,'pasaje' , 'pasajes','asiento' ,'asientos', 'vuelo', 'vuelos']:
                index = token.i - 1
                if doc[index].is_digit:
                    num_boletos = int(doc[index].text)
                    break

        return num_boletos