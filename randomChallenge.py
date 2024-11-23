import json
import random
from random import randrange, seed
import threading
import time
from gtts import gTTS
import pygame

# Open and read the challenge JSON file
with open('challengesData.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
challenges = data['challenges']

# Open and read the challenge JSON file
with open('challengesPunishments.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
punishments = data['punishments']

seed(time.time())

# Language in which you want to convert
language = 'en'

def selectChallenge():
    randomizedChallengeList = challenges.copy()
    random.shuffle(randomizedChallengeList)

    randomizedPunishmentList = punishments.copy()
    random.shuffle(randomizedPunishmentList)

    chosenChallenge = randomizedChallengeList[0]
    chosenPunishment = randomizedPunishmentList[0]

    challengeText = "Your challenge is: " + chosenChallenge
    punishmentText = "If you fail, your punishment will be: " + chosenPunishment

    print(challengeText)
    print(punishmentText)

    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    challenge = gTTS(text=challengeText, lang=language, slow=False)
    punishment = gTTS(text=punishmentText, lang=language, slow=False)

    # Saving the converted audio in a mp3 file
    challenge.save("challenge.mp3")
    punishment.save("punishment.mp3")

    # Initialize the mixer module
    pygame.mixer.init()

    print("Playing challenge audio...")
    # Load the mp3 file
    pygame.mixer.music.load("challenge.mp3")
    # Play the loaded mp3 file
    pygame.mixer.music.play()
    # Wait until playback is finished
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    print("Playing punishment audio...")
    # Load the mp3 file
    pygame.mixer.music.load("punishment.mp3")
    # Play the loaded mp3 file
    pygame.mixer.music.play()
    # Wait until playback is finished
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    print("Audio playback completed.")

selectChallenge()