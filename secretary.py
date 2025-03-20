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
    voices = engine.getProperty('voices')       # getting details of current voice
    engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 0 for male, 1 for female
    engine.say("Next person in line, present yourself please.")
    engine.runAndWait()

main()
