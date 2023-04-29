import argparse
import pyttsx3
import os
import openai
import dotenv
dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


parser = argparse.ArgumentParser(description='Epic Battle Simulator')
# params: tts boolean (default: False)
parser.add_argument('--tts', action='store_true', help='Text to Speech')

params = parser.parse_args()

if params.tts:
    engine_tts = pyttsx3.init()


message_history = []


def speak(text):
    engine_tts.say(speak)
    engine_tts.runAndWait()


def send_to_ai(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    return response.choices[0]['message']['content']


def first_prompt():
    return """On va jouer a un jeux de rôle où deux joueur s'affrontent pour battre l'autre.
Les joueurs annoncent ce qu'ils font et tu raconte ce qu'il se passe sur un ton épique.
Il y a 3 rounds de batailles.
Aucun des joueurs ne peut mourir.
Tu finis chaque round par définir le nombre de points gagnés ou perdu avec une brêve justification
Les deux joueurs sont des humains normaux, tu devras les punir s'ils utilisent des capacités en dehors de leurs capacités. Tu devras les récompenser s'ils utilisent des actions créatives que peut faire un humain.
"""


def display_text(text):
    print(text)
    if params.tts:
        speak(text)


if __name__ == '__main__':
    print("Welcome to Epic Battle Simulator")

    message_history.append(dict(role="user", content=first_prompt()))
    message_history.append(
        dict(role="assistant", content="I understand the rules"))
    message_history.append(dict(role="user", content="""Commence par inventer la situation dans laquelle Joueur 1 et Joueur 2 se retrouvent prêt à combatre. Utilise ce format:
situation des deux joueurs: $situation"""))

    round_text_ai = send_to_ai(message_history)
    display_text(round_text_ai)
    message_history.append(dict(role="assistant", content=round_text_ai))

    for _ in range(3):

        action_j1 = input("Joueur 1: ")
        action_j2 = input("Joueur 2: ")
        action_j1 = "Joueur 1: " + action_j1
        action_j2 = "Joueur 2: " + action_j2

        round_text_user = action_j1 + "\n" + action_j2

        message_history.append(dict(role="user", content=round_text_user))
        round_text_ai = send_to_ai(message_history)
        display_text(round_text_ai)

        message_history.append(dict(role="assistant", content=round_text_ai))
