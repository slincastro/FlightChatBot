from src.extractors import airline_extractor as extractor


def test_sould_return_lufthansa_when_ask_travel_using_lufthansa():
    text = "quiero viajar el 2 de febrero de madrid a santiago en lufthansa"
    airline = extractor.AirlineExtractor({"aerolinea":None}).extract(text)
    assert airline[0] == "lufthansa"
    
def test_sould_return_iberia_when_ask_a_travel_using_iberia():
    text = "quiero viajar en iberia el 2 de febrero de madrid a santiago "
    airline = extractor.AirlineExtractor({"aerolinea":None}).extract(text)
    assert airline[0] == "iberia"
    
def test_sould_return_none_when_ask_a_travel_without_airline():
    text = "quiero viajar el 2 de febrero de madrid a santiago "
    airline = extractor.AirlineExtractor({"aerolinea":None}).extract(text)
    assert airline == []
    
def test_sould_return_none_when_ask_a_travel_with_airline_in_wrong_place():
    text = "quiero viajar el 2 de febrero de madrid a santiago en "
    airline = extractor.AirlineExtractor({"aerolinea":None}).extract(text)
    assert airline == []
    
def test_should_return_avianca_when_Ask_for_avianca():
    text = "en avianca"
    airline = extractor.AirlineExtractor({"aerolinea":None}).extract(text)
    assert airline[0] == "avianca"
    
def test_should_return_avianca_when_Ask_for_avianca_with_spaces():
    text = "en avianca "
    airline = extractor.AirlineExtractor({"aerolinea":None}).extract(text)
    assert airline[0] == "avianca"
    
def test_should_return_emirates_when_ask_for_emirates():
    text = "en emirates"
    airline = extractor.AirlineExtractor({"aerolinea":None}).extract(text)
    assert airline[0] == "emirates"
    
def test_should_return_emirates_when_ask_for_emirates_with_spaces():
    text = "en emirates "
    airline = extractor.AirlineExtractor({"aerolinea":None}).extract(text)
    assert airline[0] == "emirates"
    
def test_should_retur_latam_when_ask_for_latam():
    text = "en latam"
    airline = extractor.AirlineExtractor({"aerolinea":None}).extract(text)
    assert airline[0] == "latam"