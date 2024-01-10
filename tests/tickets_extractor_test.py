from src.extractors import ticket_extractor as extractor
from src.extractors.dictionaries import numbers 


def test_shoud_return_2_whet_ask_for_2_tickets():
    text = "Quiero reservar dos boletos"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 2
    
def test_shoud_return_3_whet_ask_for_3_tickets():
    text = "Quiero comprar tres asientos"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 3
    
def test_shoud_return_4_whet_ask_for_4_tickets():
    text = "necesito comprar cuatro asientos"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 4    
    
def test_shoud_return_5_whet_ask_for_5_tickets():
    text = "deme cuatro"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 4 

def test_shoud_return_6_whet_ask_for_6_tickets():
    text = "seis"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 6

def test_shoud_return_7_whet_ask_for_7_tickets():
    text = "quiero siete vuelos"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 7 
    
def test_shoud_return_8_whet_ask_for_8_tickets():
    text = "quiero ocho asientos para mi viaje"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 8
    
def test_shoud_return_9_whet_ask_for_9_tickets():
    text = "necesito nueve boletos para mi viaje"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 9
