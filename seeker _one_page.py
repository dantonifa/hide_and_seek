"""BYU CSE210 Week 03 Assignment: Seeker, a project to import modules.
Seeker is played according to the following rules.

1. The hider's location is a random number between 1 and 1000.
2. The seeker searches for the hider by guessing its location.
3. If the guess is closer to the hider's location it says, "Getting warmer!"
4. If the guess is farther away from the hider's location it says, "Getting colder!"
5. If the guess is correct the hider says, "You found me!". The game is over."""

import random
hider_position  = []
seeker_distance = []
class Hider():
    def __init__(self):
        self._hider_location = random.randint(1, 1000)
        hider_position.append(self._hider_location)
        print(hider_position[-1])
class Seeker_1():
    def __init__(self):
        self.x_1 = hider_position[-1]
        self.location_1()
        self.distance_1()
    def location_1(self):
        self.seeker_1st_location = int(input("Enter a location [1:1000]: "))
        return self.seeker_1st_location
    def distance_1(self):
        self.distance = abs(self.x_1 - self.seeker_1st_location)
        seeker_distance.append(self.distance)
        seeker_1_distance = seeker_distance[-1]
        print(seeker_1_distance)
        
        if self.distance == 0:
            print("(;.;) You found me!")
            exit()
        elif self.distance <= self.seeker_1st_location: 
            print("(>.<) Getting warmer!")
        elif self.distance > self.seeker_1st_location:
            print("(^.^) Getting colder!")
class Seeker_2(Hider, Seeker_1):
    def __init__(self):
        self.location_2()
        self.distance_2()
    def location_2(self):
        self.seeker_2nd_location = int(input("Enter a location [1:1000]: "))
    def distance_2(self):
        self.second_distance = abs(hider_position[-1] - self.seeker_2nd_location)
        if self.second_distance == 0:
            print("(;.;) You found me!")
            exit() 
        elif self.second_distance > seeker_distance[-1]:
            print("(^.^) Getting colder!")
        elif self.second_distance < seeker_distance[-1]:
            print("(>.<) Getting warmer!")
        Terminal()
        
class Terminal():
    def __init__(self):
        Seeker_2()
    
def main():
    Hider()
    Seeker_1()
    Seeker_2()
   
if __name__=="__main__":
   main()  

    
    
    
    
               
