import random
import time
from pygame import mixer

mixer.init()
clothesline_se = mixer.Sound("audio/clothesline.wav")
bodyslam_se = mixer.Sound("audio/bodyslam.wav")
special_se = mixer.Sound("audio/finisher.wav")

class Character():
    def __init__(self, name, health, clothesline_power, bodyslam_power, special_power, special_name):
        self.name = name
        self.health = health
        self.clothesline_power = clothesline_power
        self.bodyslam_power = bodyslam_power
        self.special_power = special_power
        self.special_name = special_name
        

    def __str__(self):
        return """
        Name: %s
        Health: %s
        clothesline Power: %s
        bodyslam Power: %s
        Special Power: %s (%d)
        
        """ % (self.name, self.health, self.clothesline_power, self.bodyslam_power, self.special_name, self.special_power)

    def bodyslam(self, opponent):
        if self.bodyslam_power == "low":
            bodyslam = random.randint(1, 3)
        if self.bodyslam_power == "medium":
            bodyslam = random.randint(4, 6)
        if self.bodyslam_power == "high":
            bodyslam = random.randint(7, 9)
        opponent.health -= (bodyslam)
        mixer.Sound.play(bodyslam_se)
        time.sleep(1)
        print("\n\n%s bodyslammed for %d damage to %s." %
              (self.name, bodyslam, opponent.name))
        print("%s has %d health left." %
              (opponent.name, opponent.health))

    def clothesline(self, opponent):
        if self.clothesline_power == "low":
            clothesline = random.randint(1, 3)
        if self.clothesline_power == "medium":
            clothesline = random.randint(4, 6)
        if self.clothesline_power == "high":
            clothesline = random.randint(7, 9)
        opponent.health -= (clothesline)
        mixer.Sound.play(clothesline_se)
        time.sleep(1)
        print("\n\n%s clotheslined for %d damage to %s." %
              (self.name, clothesline, opponent.name))
        print("%s has %d health left." %
              (opponent.name, opponent.health))

    def special(self, opponent):
        opponent.health -= (self.special_power)
        mixer.Sound.play(special_se)
        time.sleep(4)
        print("\n\n%s used %s for %d damage to %s." %
              (self.name, self.special_name, self.special_power, opponent.name))
        print("%s has %d health left." %
              (opponent.name, opponent.health))

    def rand_attack(self, opponent):
        random_selection = random.randint(1, 3)
        if random_selection == 1:
            self.clothesline(opponent)
        if random_selection == 2:
            self.bodyslam(opponent)
        if random_selection == 3:
            self.special(opponent)

    def is_alive(self):
        return self.health > 0

