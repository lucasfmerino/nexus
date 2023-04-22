import speech_recognition as sr
import webbrowser
import pyautogui
import time

# Inicializa o recognizer
r = sr.Recognizer()

# Loop principal para escutar comandos de voz
while True:
    with sr.Microphone() as source:
        print("Nexus: Ouvindo...")
        audio = r.listen(source)

        try:
            # Usa o Google Speech Recognition para converter o áudio em texto
            command = r.recognize_google(audio, language='pt-BR')

            # Verifica se o comando contém "nexus pesquisar"
            if "nexus pesquisar" in command.lower():
                # Extrai o termo de pesquisa
                search_term = command.lower().replace("nexus pesquisar", "")
                search_term = search_term.strip()

                # Abre o navegador e pesquisa o termo no Google
                url = "https://www.google.com/search?q={}".format(search_term)
                webbrowser.get().open(url)
                print("Nexus: Pesquisando por '{}' no Google...".format(search_term))

            elif "nexus tocar música" in command.lower():
                # Extrai o nome da música
                music_name = command.lower().replace("nexus tocar música", "")
                music_name = music_name.strip()

                # Abre o navegador e toca a música no Spotfy
                url = f"https://open.spotify.com/?autoplay=true"
                webbrowser.get().open(url)
                print(f"Nexus: Tocando música no Spotify...")

                # Simula as teclas de atalho para iniciar a música
                time.sleep(5)  # aguarda 5 segundos para usar o comando
                pyautogui.hotkey('space')

            elif "nexus parar música" in command.lower():
                # Simula as teclas de atalho para parar a música
                pyautogui.hotkey('space')

            elif "nexus retomar música" in command.lower():
                # Simula as teclas de atalho para tocar a música
                pyautogui.hotkey('space')

            # Verifica se o comando é "nexus desligar" para e ncerrar o programa
            elif "nexus desligar" in command.lower():
                print("Nexus: Encerrando o programa...")
                break

        except sr.UnknownValueError:
            print("Nexus: Não entendi o comando de voz.")
