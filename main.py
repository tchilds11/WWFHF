import random
import time
from text import story, title, fight_text, game_over, sucking, loading, ending_story, choose
from classes import Character
from functions import player_selection, ending, character_list, sound, player_defeated, opponent_lose_action
import sys

# Music
from pygame import mixer
mixer.init()
mixer.music.load("audio/doomhulk.mp3")
mixer.music.play(0)


def keep_playing():
    while len(opponent_list) >= 1:
        keep_playing = input("Do you want to keep fighting? (y or n) ")
        if keep_playing == 'y':
            player.health = 50
            print("\nYou ate your protien bar!!")
            print("You're back to Full Health: %d \n" % (player.health))
            print("Your next challenger is: %s" % (opponent_list[0]))
            play_list.pop(0)

            for num in play_list:
                if num == play_list[0]:
                    sound("buffer.wav")

            time.sleep(0)
            fight_text()
            sound("bell.wav")
            fight()
        elif keep_playing == 'n':
            print("Cain't win it if Ya ain't in it\n\n")
            game_over()
            sys.exit(0)
        else:
            sound("bell.wav")
            print("your fingers need some exersice\n")


def attack(type, opponent_list):
    # Player attacks opponent
    type(opponent_list[0])
    # mixer.Sound.play(special_se)
    time.sleep(1.5)
    if opponent_list[0].is_alive() == False:
        opponent_lose_action(opponent_list)
        if len(opponent_list) >= 1:
            keep_playing()
            play_list.pop(0)
        else:
            ending()


# In ring action
def fight():

    while opponent_list[0].health > 0 and player.health > 0:
        
        print("\nWhat do you want to do?")
        print("1. bodyslam")
        print("2. clothesline")
        print("3. %s" % (player.special_name))
        print("4. I'm out")
        print(">>> ",)
        user_input = input()
# bodyslam
        if user_input == "1":
            attack(player.bodyslam, opponent_list)
# clothesline
        elif user_input == "2":
            attack(player.clothesline, opponent_list)
# Special
        elif user_input == "3":
            attack(player.special, opponent_list)
# # Cheat

#         elif user_input =="8675309"
#             attack(player.jenny, opponent_list)

# Take this job and shove it!!
        elif user_input == "4":
            print("Cain't win it if ya ain't in it")
            sound("strategy.wav")
            time.sleep(10)
            sys.exit(0)
        else:
            sound("strategy.wav")
            print(
                "What the hell are you doing?\n")
            time.sleep(5)
# Heel Attacks
        if player.health > 0:
            # Opponent attacks player
            opponent_list[0].rand_attack(player)
            if player.is_alive() == False:
                player_defeated(player)


                # print title screen
title()


time.sleep(4)
sound("bell.wav")
input("Press enter to continue\n \n \n")

choose()
player = player_selection()
character_list = character_list()
opponent_list = []
for character in character_list:
    if player != character:
        opponent_list.append(character)


play_list = ['1', '2', '3', '4', '5', '6', '7', '8']

# when user selects a character, it moves remaining characters to opponents list for battle


print("You have choosen %s" % (player))


print()
time.sleep(1)
story()
time.sleep(3)
ready = input("\nAre you ready to fight? (y or n) ")
if ready == "y":
    print("\nGET READY!\n")
    sound("buffer.wav")
else:
    print("\nThen, get read for an ass whoopin\n")
    time.sleep(3)
    sound("buffer.wav")

print("\nYour first opponent is: %s" % (opponent_list[0]))
time.sleep(2)
fight_text()
sound("bell.wav")

fight()
