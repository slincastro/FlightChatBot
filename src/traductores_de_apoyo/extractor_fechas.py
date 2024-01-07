import re

class ExtractorFechas:
    def __init__(self):
        self.patron_fecha = r'\b\d{1,2}\sde\s(?:enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)(?:\sde\s\d{4})?\b'

    def extraer_fecha(self, texto):
        fecha_larga = self.extraer_fecha_larga(texto)
        if fecha_larga:
            return fecha_larga
        else:
            return self.extraer_fecha_corta(texto)
        
    def extraer_fecha_larga(self, texto):
        fecha = re.search(self.patron_fecha, texto)
        if fecha:
            fecha_encontrada = fecha.group()
            return fecha_encontrada
        else:
            return None

    def extraer_fecha_corta(self, texto):
        fecha = re.search(r'\b\d{1,2}/\d{1,2}/\d{4}\b', texto)
        if fecha:
            fecha_encontrada = fecha.group()
            return fecha_encontrada
        else:
            return None