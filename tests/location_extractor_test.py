from src.extractors.location_extractor import LocationExtractor

def test_should_return_londres_when_ask_for_travel_from_londres_to_madrid():
    text = "quiero viajar de Londres a Madrid"
    llamada_reserva = {"origen":None, "destino":None}
    origen = LocationExtractor(llamada_reserva).extract_origen(text)
    
    assert origen == "Londres"
    
def test_should_return_madrid_when_ask_for_travel_from_londres_to_madrid():
    text = "quiero viajar de Londres a Madrid"
    llamada_reserva = {"origen":None, "destino":None}
    destino = LocationExtractor(llamada_reserva).extract_destino(text)
    
    assert destino == "Madrid"
    
def test_should_return_quito_when_ask_for_travel_from_quito_to_madrid():
    text = "quiero viajar a Madrid de Quito"
    llamada_reserva = {"origen":None, "destino":None}
    origen = LocationExtractor(llamada_reserva).extract_origen(text)
    
    assert origen == "Quito"
    
def test_should_return_bogota_when_ask_for_travel_from_quito_to_bogota():
    text = "quiero viajar a Bogotá desde Quito"
    llamada_reserva = {"origen":None, "destino":None}
    origen = LocationExtractor(llamada_reserva).extract_destino(text)
    
    assert origen == "Bogotá"
    
def test_should_return_santiago_and_guayaquil_when_ask_for_travel_from_santiago_to_guayaquil():
    text = "quiero viajar de Santiago a Guayaquil"
    llamada_reserva = {"origen":None, "destino":None}
    origen, destino = LocationExtractor(llamada_reserva).extract(text)
    
    assert origen == "Santiago"
    assert destino == "Guayaquil"
    
def test_should_return_from_santiago_to_guayaquil_when_ask_for_travel_from_santiago_to_guayaquil():
    text = "quiero viajar a Guayaquil desde Santiago"
    llamada_reserva = {"origen":None, "destino":None}
    origen, destino = LocationExtractor(llamada_reserva).extract(text)
    
    assert origen == "Santiago"
    assert destino == "Guayaquil"