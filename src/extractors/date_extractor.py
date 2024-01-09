import re

class DateExtractor:
    def __init__(self):
        self.patron_fecha_larga = r'\b\d{1,2}\sde\s(?:enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)(?:\sde\s\d{4})?\b'
        self.patron_fecha_corta = r'\b\d{1,2}/\d{1,2}/\d{4}\b'
        self.patron_primero_de_mes = r'\bprimero\sde\s(?:enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\b'

    def extract(self, texto):
        fechas_largas = self.extraer_fechas_largas(texto)
        fechas_cortas = self.extraer_fechas_cortas(texto)
        fechas_primero_de_mes = self.extraer_fechas_primero_de_mes(texto)
        return fechas_largas + fechas_cortas + fechas_primero_de_mes

    def extraer_fechas_largas(self, texto):
        return re.findall(self.patron_fecha_larga, texto)

    def extraer_fechas_cortas(self, texto):
        return re.findall(self.patron_fecha_corta, texto)

    def extraer_fechas_primero_de_mes(self, texto):
        return re.findall(self.patron_primero_de_mes, texto)