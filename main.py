from modules.text_to_speech import text_to_speech
from modules.speech_to_text import speech_to_text
from modules.actions import search_wikipedia, open_youtube, find_nearest_pharmacy

def main():
    text_to_speech("Como posso ajudar você?")
    command = speech_to_text()
    
    if "Wikipedia" in command:
        query = command.replace("Wikipedia", "").strip()
        search_wikipedia(query)
    elif "YouTube" in command:
        open_youtube()
    elif "farmácia mais próxima" in command:
        find_nearest_pharmacy()
    else:
        text_to_speech("Desculpe, não entendi o comando.")

if __name__ == "__main__":
    main()
