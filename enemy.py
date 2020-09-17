""""" This class contains all the things our players will have to fight.
This will also store hit points and number of lives.
-We will initialize attributes for those.
-This file is for use with Player_Inheritance and main_Inheritance"""

import random


class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1): #__init__ is a Constructor
        self.name = name              # attribute
        self.hit_points = hit_points  # attribute
        self.lives = lives             # attribute
        self.alive = True
        # This is a superclass and any class that extends this class or
        # inherits from this class, Enemy should always have name, hit points,
        # and lives attributes

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            # self.hit_points gets new value of 'remaining_points"
            print(" I took {} points damage and have {} left".format(damage, self.hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                print("{0.name} lost a life".format(self))
            else: #case where there's 0 lives left
                print("{0.name} is dead".format(self))
                self.alive = False

            # if remaining_points drop below 0, then 1 life is taken instead
            # therefore, if points drops below hit_points, then lives drops by 1 and you keep
            # the value of the hit_points

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit Points: {0.hit_points}".format(self)
        # will take all the attributes from __init__


"""Troll will inherit traits from the Enemy class. Troll is now a subclass of Enemy"""
class Troll(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)
       # Enemy.__init__(self, name=name, lives=1, hit_points=23)
       # super helps you cope with Multiple Inheritance instead of specifying the base class
       # Enemy is the superclass

    def grunt(self):
        print("Me {0.name}, {0.name} stomp you".format(self))


"""Vampire will inherit traits from the Enemy class. Vampire is now a subclass of Enemy"""
class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self):
        if random.randint(1,3) == 3:  # random int generated between 1 and 3
            print("***** {0.name} dodges *****".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage) # Here we called the superclasses take_damage() method


class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name) #the super of this class is Vampire, not Enemy
        #which is why we only pass 'name' and not lives or hit_points.

        self.hit_points = 140

    def take_damage(self, damage): # We are going to override this method specifically for VampireKing
        super().take_damage(damage // 4)

















