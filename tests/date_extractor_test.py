from src.extractors import date_extractor as extractor

llamada = {"fecha":None}

def test_should_return_date_when_date_in_short_format_is_in_text():
    
    text = "El vuelo sale el 12/12/2020"
    date = extractor.DateExtractor(llamada).extract(text)
    assert date[0] == "12/12/2020"
    
def test_should_return_date_when_date_in_long_format_is_in_text():
    text = "El vuelo sale el 12 de diciembre de 2020"
    date = extractor.DateExtractor(llamada).extract(text)
    assert date[0] == "12 de diciembre de 2020"
    
def test_should_return_none_when_no_date_is_in_text():
    text = "El vuelo sale mañana"
    date = extractor.DateExtractor(llamada).extract(text)
    assert date == []
    
def test_should_return_date_when_date_in_long_format_is_in_text_without_year():
    text = "El vuelo sale el 12 de diciembre"
    date = extractor.DateExtractor(llamada).extract(text)
    assert date[0] == "12 de diciembre"
    
def test_should_return_none_when_no_date_but_number_is_in_text():
    text = "El vuelo sale mañana a las 12"
    date = extractor.DateExtractor(llamada).extract(text)
    assert date == []