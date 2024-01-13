import spacy
import re

class AirportExtractor():
    def __init__(self, llamada_reserva):
        self.llamada_reserva = llamada_reserva
        
    def extract(self, text):
       return text
    
    def get_text_numbers(self):
        diccionario = {
            'uno': 1,
            'dos': 2,
            'tres': 3,
            'cuatro': 4,
            'cinco': 5,
            'seis': 6,
            'siete': 7,
            'ocho': 8,
            'nueve': 9,
            'diez': 10,
            'once': 11,
            'doce': 12,
            'trece': 13,
            'catorce': 14,
            'quince': 15,
            'dieciséis': 16,
            'diecisiete': 17,
            'dieciocho': 18,
            'diecinueve': 19,
            'veinte': 20,
            'veintiuno': 21,
            'veintidós': 22,
            'veintitrés': 23,
            'veinticuatro': 24,
            'veinticinco': 25,
            'veintiséis': 26,
            'veintisiete': 27,
            'veintiocho': 28,
            'veintinueve': 29,
            'treinta': 30,
            'treinta y uno': 31,
            'treinta y dos': 32,
            'treinta y tres': 33,
            'treinta y cuatro': 34,
            'treinta y cinco': 35,
            'treinta y seis': 36,
            'treinta y siete': 37,
            'treinta y ocho': 38,
            'treinta y nueve': 39,
            'cuarenta': 40,
            'cuarenta y uno': 41,
            'cuarenta y dos': 42,
            'cuarenta y tres': 43,
            'cuarenta y cuatro': 44,
            'cuarenta y cinco': 45,
            'cuarenta y seis': 46,
            'cuarenta y siete': 47,
            'cuarenta y ocho': 48,
            'cuarenta y nueve': 49,
            'cincuenta': 50
        } 
        
        return diccionario
    
    def specific_extraction(self, text):
        
        numeros = re.findall(r'\d+', text)

        if numeros:
            numero_vuelos = numeros[0]
            return numero_vuelos
        
        diccionario = self.get_text_numbers()
        
        modelo = spacy.load("./ticket-model")
        doc = modelo(text)
        tickets = [ent.text for ent in doc.ents]
        print(tickets)
        if len(tickets) == 0:
            return None
        if tickets[0] not in diccionario:
            return None
        number = diccionario[tickets[0]]
        self.llamada_reserva["cantidad"] = number
        return number
