import speech_recognition as sr
import webbrowser
import pyautogui
import time


r = sr.Recognizer()

commands = """
* Nexus Pesquisar [parêmetro]:
    - Abre o navegador e pesquisa o parâmetro informado no google.

* Nexus Tocar Música:
    - Abre o spotfy no navegador e inicia a música.
    - Necessário o usuário manter o Spotfy logado.

* Nexus Parar Música:
    - Pausa a música atual.

* Nexus Retomar Música:
    - Retoma a música atual.

* Nexus Desligar:
    - Encerra o Nexus.

"""

print(commands)

while True:
    with sr.Microphone() as source:
        print("Nexus: Ouvindo...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio, language='pt-BR')

            if "nexus pesquisar" in command.lower():
                search_term = command.lower().replace("nexus pesquisar", "")
                search_term = search_term.strip()
                url = "https://www.google.com/search?q={}".format(search_term)
                webbrowser.get().open(url)
                print("Nexus: Pesquisando por '{}' no Google...".format(search_term))

            elif "nexus tocar música" in command.lower():
                url = f"https://open.spotify.com/?autoplay=true"
                webbrowser.get().open(url)
                print(f"Nexus: Aguarde um momento...")
                time.sleep(5)
                pyautogui.hotkey('space')
                print(f"Nexus: Tocando música no Spotify...")


            elif "nexus parar música" in command.lower():
                pyautogui.hotkey('space')

            elif "nexus retomar música" in command.lower():
                pyautogui.hotkey('space')

            elif "nexus desligar" in command.lower():
                print("Nexus: Encerrando o programa...")
                break

        except sr.UnknownValueError:
            print("Nexus: Não entendi o comando de voz.")
