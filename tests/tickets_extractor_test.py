from src.extractors import ticket_extractor as extractor


def test_should_return_2_whet_ask_for_2_tickets():
    text = "Quiero reservar dos boletos"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 2
    
def test_should_return_3_whet_ask_for_3_tickets():
    text = "Quiero comprar tres asientos"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 3
    
def test_should_return_4_whet_ask_for_4_tickets():
    text = "necesito comprar cuatro asientos"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 4    
    
def test_should_return_5_whet_ask_for_5_tickets():
    text = "deme cinco"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 5 

def test_should_return_6_whet_ask_for_6_tickets():
    text = "seis"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 6

def test_should_return_7_whet_ask_for_7_tickets():
    text = "quiero siete vuelos"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 7 
    
def test_should_return_8_whet_ask_for_8_tickets():
    text = "quiero ocho asientos para mi viaje"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 8
    
def test_should_return_9_whet_ask_for_9_tickets():
    text = "necesito nueve boletos para mi viaje"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 9

def test_should_return_10_whet_ask_for_10_tickets():
    text = "necesito diez tickets para mi viaje"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 10
    
def test_should_return_11_whet_ask_for_11_tickets():
    text = "me gustarian once asientos"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 11
    
def test_should_return_12_whet_ask_for_12_tickets():
    text = "me gustarian doce tickets"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 12
    
def test_should_return_1_whet_ask_only_for_1_ticket():
    text = "uno"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 1
    
def test_should_return_2_whet_ask_only_for_2_tickets():
    text = "dos"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 2

def test_should_return_3_whet_ask_only_for_3_tickets():
    text = "tres"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 3
    
def test_should_return_4_whet_ask_only_for_4_tickets():
    text = "cuatro"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 4
    
def test_should_return_5_whet_ask_only_for_5_tickets():
    text = "cinco"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 5
    
def test_should_return_6_whet_ask_only_for_6_tickets():
    text = "seis"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 6
    
def test_should_return_7_whet_ask_only_for_7_tickets():
    text = "siete"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 7
    
def test_should_return_8_whet_ask_only_for_8_tickets():
    text = "ocho"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 8

def test_should_return_9_whet_ask_only_for_9_tickets():
    text = "nueve"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 9
    
def test_should_return_10_whet_ask_only_for_10_tickets():
    text = "diez"
    number = extractor.TicketExtractor({"cantidad":None}).specific_extraction(text)
    assert number == 10