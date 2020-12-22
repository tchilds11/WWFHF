import time
import sys
from pygame import mixer
from classes import Character
from text import victory, ending_story, sucking


mixer.init()


# Character Functions and Definitions

character1 = Character("Bum Bum Bichette", 50, "high", "high",
                       30, "Bum Rush")
character2 = Character("The Paper", 50, "medium", "low",
                       30, "Have you seen my Stapler")
character3 = Character("The Scissors", 50, "low",
                       "high", 30, "The Peoples eyeball")
character4 = Character("Pat the Cat", 50, "high",
                       "medium", 30, "the sandbox")
character5 = Character("Luke Warm Jim Davis", 50, "low", "low",
                       30, "Day old coffee")
character6 = Character("The Real American", 50, "high", "low", 30,
                       "Atomic Bomb")
character7 = Character("Ultimate Employee", 50, "high", "low",
                       30, "The TPS Report")
character8 = Character("Specialist Slacker", 50, "high",
                       "medium", 30, "The 'Appointment'")
character9 = Character("Tu'oh Tu'oh", 50, "high", "high",
                       30, "Pandemic")


def character_list():
    return [character1, character2, character3, character4, character5, character6, character7, character8, character9]


def print_character_menu(pos1, char1, pos2, char2, pos3, char3):
    print("-" * 110)
    print("{:<15}|| {:<30}|| {:<30}|| {:<30}|".format(
        "Name:", (pos1 + char1.name), (pos2 + char2.name), (pos3 + char3.name)))
    print("{:<15}|| {:<30}|| {:<30}|| {:<30}|".format(
        "Health:", char1.health, char2.health, char3.health))
    print("{:<15}|| {:<30}|| {:<30}|| {:<30}|".format(
        "clothesline:", char1.clothesline_power.title(), char2.clothesline_power.title(), char3.clothesline_power.title()))
    print("{:<15}|| {:<30}|| {:<30}|| {:<30}|".format(
        "bodyslam:", char1.bodyslam_power.title(), char2.bodyslam_power.title(), char3.bodyslam_power.title()))
    print("{:<15}|| {:<30}|| {:<30}|| {:<30}|".format(
        "Special:", char1.special_name, char2.special_name, char3.special_name))
    print("-" * 110)


def player_selection():
    print_character_menu("1. ", character1, "2. ",
                         character2, "3. ", character3)
    print_character_menu("4. ", character4, "5. ",
                         character5, "6. ", character6)
    print_character_menu("7. ", character7, "8. ",
                         character8, "9. ", character9)

# Looping user input to choose character
    while True:
        character_choice = input("Choose the descructor (1-9) ")
        if character_choice == "1":
            player = character1
            return player
        elif character_choice == "2":
            player = character2
            return player
        elif character_choice == "3":
            player = character3
            return player
        elif character_choice == "4":
            player = character4
            return player
        elif character_choice == "5":
            player = character5
            return player
        elif character_choice == "6":
            player = character6
            return player
        elif character_choice == "7":
            player = character7
            return player
        elif character_choice == "8":
            player = character8
            return player
        elif character_choice == "9":
            player = character9
            return player
        else:
            sound("bell.wav")
            print("Any number between 1 and 9. Can you not count?")


# Gameplay Functions

def sound(file):
    sound = mixer.Sound("audio/%s" % file)
    return mixer.Sound.play(sound)


def opponent_lose_action(opponent_list):
    print("%s ran home to his mommy.\n" % (opponent_list[0].name))
    print("")
    sound("pinfall.wav")
    victory()
    opponent_list.pop(0)


def player_defeated(player):
    print("%s has lost.\n\n" % (player.name))
    sucking()
    sound("sucks.wav")
    time.sleep(60)
    print("Better luck next time, chump.")
    time.sleep(5)
    sys.exit(0)


def ending():
    time.sleep(1.5)
    ending_story()
    #insert music on this line
    time.sleep(5)
    sys.exit(0)
