from src.driven_adapters.airport_client import AirportClient

class AirportExtractor():
    def __init__(self, llamada_reserva):
        self.llamada_reserva = llamada_reserva
        
    def extract(self, text):
        airport = AirportClient().get_airport(text)
        if airport:
            self.llamada_reserva["aeropuerto"] = airport
        return airport