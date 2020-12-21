import random

class Face():
    def __init__(self, name, health, clothesline_power, bodyslam_power, special_power):
        self.name = name 
        self.health = health
        self.clothesline_power = clothesline_power
        self.bodyslam_power = bodyslam_power
        self.special_power = special_power

    
    def __str__(self):
        return """
        Name: %s
        Health: %s
        Clothesline Power: %s
        Bodyslam Power: %s
        Special Power: %s (%d)
        """ % (self.name, self.health, self.clothesline_power, self.bodyslam_power, self.special_power)

    
    def clothesline(self, heel):
        if self.clothesline_power == "weak":
            clothesline = random.randint(1, 5)
        health = heel.health
        heel.health -= (clothesline)
        print("\n\n%s clotheslined for %d damage to %s." %
              (self.name, clothesline, heel.name))

    def bodyslam(self, heel):
        if self.bodyslam_power == "medium":
            bodyslam = random.randint(6, 10)
        health = heel.health
        heel.health -= (bodyslam)
        print("\n\n%s Oh! Bodyslam! %s took %d damage!" %
              (self.name, bodyslam, heel.name))

    def special(self, heel):
        if self.special_power == "strong":
            special = random.randint(11,20)
        health = heel.health
        heel.health -= (special)
        print("\n\n%s It has to be over! %d damage done to %s!" %
                (self.name, special, heel.name))            

    def be_alive(self):
        self.health > 0

    def print_status(self):
        print("You have %d health." % (self.health))

class Heel:
    def __init__(self, name, health, power, attack):
        self.power = power
        self.name = name 
        self.dropkick = dropkick = 10
        self.suplex = suplex = 15
        self.special = special = 20
        self.health = health = 100

    # Heel Attack Face
    # def attack(self, Face):
    #     heel.health -= self.power
    #     print("The Heel does (self.power) damage to you.")
    #     heel.health -= self.dropkick 
    #     print("Lookout! Dropkick!")
    #     heel.health -= self.suplex
    #     print("Oh no! Suplex!")
    #     heel.health -= self.special
    #     print("Bah Gawd! That man has a family dammit!")


    def be_alive(self):
        self.health > 0

heel = Heel(10, 10, 10, 10)
face = Face(10, 100, "weak", "medium", "strong")

while heel.health > 0 and face.health > 0:
        print("You have %d health" % (face.health))
        print("Opponent has %d health" % (heel.health))
        print("What do you want to do?")
        print("1. Clothesline")
        print("2. Body Slam")
        print("3. Special")
        print(">>> ",)

        user_input = input()

        if user_input == "1":
            face.clothesline(heel)
        #     health = heel.health
        #     heel.health -= (health - clothesline)
        #     print("\n\n%s clotheslined for %d damage to %s." %
        #       (self.name, clothesline, opponent.name))

        elif user_input == "2":
            face.bodyslam(heel)
            # heel.health -= face.bodyslam_power
            # print("Ouch! You did %d damage to the heel!" % face.bodyslam_power)

        elif user_input == "3":
            face.special(heel)
            # heel.health -= face.special_power
            # print("That has to be it!!! You did %d damage to the heel!" % face.special_power)

        else:
            print("You're not the keyboard warrior I thought you were! Try again punk! %r" %user_input)  

        if heel.health <= 0:
                print("Andddddd NEWWWWWWWWW Heavyweight Champion!")

        if heel.health > 0:
            face.health -= heel.power
            print("The heel does %d damage to you!" % heel.power)
            if face.health <= 0:
                print("You just got knocked the F out!")

def keep_playing():
    while len(opponent_list) >= 1:
         if keep_playing == 'y':
             player.health = 50 
             print("n\You ate a protein bar!")
             print("Go kick some ass!: %d \n" % (player.health))
             print("Your next opponent is: %s" % (opponent_list[0]))
            
         elif keep_playing == 'n':
            print("I told you, i'm the best there is, the best there was, and the best there ever will be!\n\n")
