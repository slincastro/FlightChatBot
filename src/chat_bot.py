import spacy
from spacy.matcher import Matcher
import traductores_de_apoyo.extractor_fechas as extractor

nlp = spacy.load("es_core_news_sm")


matcher = Matcher(nlp.vocab)

pattern_reservar = [{"LOWER": "reservar"}, {"LOWER": "vuelo"}]
pattern_cancelar = [{"LOWER": "cancelar"}, {"LOWER": "reserva"}]
matcher.add("RESERVAR_VUELO", [pattern_reservar])
matcher.add("CANCELAR_RESERVA", [pattern_cancelar])

# Función para procesar la entrada del usuario
def process_input(user_input):
    
    doc = nlp(user_input)
    
    fecha = extractor.ExtractorFechas().extraer_fecha(user_input)
    print(fecha)
    
    stop_words_modificadas = nlp.Defaults.stop_words - {"de", "a", "desde", "hasta", "hacia"}

    # Eliminando puntuación y convirtiendo a minúsculas
    tokens_limpios = [token.text.lower() for token in doc if not token.is_punct]
    print("="*30)
    print(tokens_limpios)
    # Eliminando stop words (palabras comunes)
    tokens_sin_stopwords = [token.text.lower() for token in doc if token.text.lower() not in stop_words_modificadas]

    print(tokens_sin_stopwords)
    
    matches = matcher(doc)

    # Identificar intención
    for match_id, start, end in matches:
        rule_id = nlp.vocab.strings[match_id]
        if rule_id == "RESERVAR_VUELO":
            return handle_reservar_vuelo(doc)
        elif rule_id == "CANCELAR_RESERVA":
            return handle_cancelar_reserva(doc)

    # Extracción de entidades comunes
    for ent in doc.ents:
        print(f"{ent.text} - {ent.label_}")

    return "No estoy seguro de cómo ayudar con eso."

# Funciones para manejar intenciones específicas
def handle_reservar_vuelo(doc):
    return "Vamos a reservar tu vuelo."

def handle_cancelar_reserva(doc):
    return "Tu reserva ha sido cancelada."


while True:
    user_input = input("Tú: ")
    if user_input.lower() == "salir":
        break
    response = process_input(user_input)
    print("Chatbot:", response)
