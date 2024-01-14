#FlightChatBot

Este chatbot esta optimizado para mac, en windows por el momento esta en modo beta, aun presenta algunas fallas de funcionamiento

2.- Entrar a la carpeta FligthChatbot:

`cd FligthChatbot`

3.- Instalar las dependencias, se puede instalar una a una las dependencias :

usar el comando : 

`pip3 install -r requirements.txt`

4.- Ejecutar la aplicación :

`python3 src/chatbot.py`

5.- Ejecutar pruebas :

`pytest`



-------------------------------------------

Para instalar las dependencias una a una :

pip3 install spacy
python -m spacy download es_core_news_sm
pip3 install SpeechRecognition pyaudio
brew install portaudio
pip3 install word2number
pip3 install inflect
pip3 install num2words
pip3 install googletrans

Para windows + conda :

pip3 install spacy
python -m spacy download es_core_news_sm
pip3 install pyttsx3
pip3 install SpeechRecognition
pip3 install requests
pip3 install dateparser
conda install pyaudio.
conda install -c anaconda portaudio.



