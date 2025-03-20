import pygame
import pyttsx3

pygame.init()

def main():
    play_music()
    text_to_speech()

def play_music() :
    sound = pygame.mixer.Sound("Windows95_Startup.mp3")
    pygame.mixer.Sound.play(sound)
    pygame.time.wait(7000)

def text_to_speech() :
    engine = pyttsx3.init()
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0"
    # Getting the french voice and setting it as voice_id
    engine.setProperty("voice",voice_id)
    engine.say("Personne suivante, s'il vous plaît.")
    engine.runAndWait()

def get_input() :
    user_input = str(input("Quel est votre nom, s'il vous plaît ?"))
    return user_input

def names_list() :
    names = []
    user_input = get_input()
    names.append(user_input)


main()

