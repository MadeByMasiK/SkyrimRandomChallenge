import json
import random
from random import randrange, seed
import threading
import time
from gtts import gTTS
import pygame
import os

# Open and read the challenge JSON file
with open('challengesData.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
challenges = data['challenges']

# Open and read the challenge JSON file
with open('challengesPunishments.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
punishments = data['punishments']

# Language in which you want to convert
language = 'en'

def selectChallenge():
    seed(time.time())

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

    # File paths
    challenge_file = "challenge.mp3"
    punishment_file = "punishment.mp3"

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
    # Stop music before removing the files
    pygame.mixer.music.stop()
    # Explicitly quitting the mixer to release the files
    pygame.mixer.quit()
    # Short delay to allow for resource cleanup
    time.sleep(0.1)

    print("Audio playback completed.")

    # Now remove the audio files after playback
    if os.path.exists(challenge_file):
        os.remove(challenge_file)
    if os.path.exists(punishment_file):
        os.remove(punishment_file)

print("Give me the minimum amount of time for the random timer:")
min_time = input()
print("Give me the maximum amount of time for the random timer:")
max_time = input()

while True:
    selectChallenge()
    random_interval = random.randint(int(min_time), int(max_time))  # Random interval between 10 and 30 minutes (600-1800 seconds)
    print(f"Next call in {random_interval / 60:.2f} minutes / {random_interval} seconds")
    time.sleep(random_interval)  # Wait for the random interval