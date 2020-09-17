from Player_Inheritance import Player
sabrina = Player("Sabrina")

from enemy import Enemy, Troll, Vampire, VampireKing


####################
##TEST VAMPIREKING##
####################

dracula = VampireKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)



##############
##TEST ENEMY##
##############
# random_monster = Enemy("Basic enemy", 12, 1)  #name, hit_points, lives
# print(random_monster)
#
# random_monster.take_damage(13) #runs take_damage class. damage=4
# print(random_monster)



##############
##TEST TROLL##
##############
# ugly_troll = Troll("Pug")  # no arguments
# ugly_troll.take_damage(10)
# print("ugly troll - {}".format(ugly_troll))
#
# another_troll = Troll("Ug")  # 3 arguments
# print("another_troll - {}".format(another_troll))
#
# brother = Troll("Urg")  # 2 arguments
# print(brother)

# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()




################
##TEST VAMPIRE##
################
# vamp = Vampire("Dracula")
# print("Vampire #1: {}".format(vamp))
#
# vamp.take_damage(13)
# print(vamp)
#
# while vamp.alive:
#     vamp.take_damage(1)
    #Even though vampire inherits from enemy, it will noe behave a but differently
    #because we over wrote the take_damage when it's specific to the vampire.
       # print(vamp) # will only print if it has taken some damage






#############################
##USED TO TEST PLAYER CLASS##
#############################
# print(sabrina.name)  # printing data attribute directly
# print(sabrina.lives)  # printing data attribute directly
# sabrina.lives -= 1
# print(sabrina)
#
# sabrina._lives = 9
# print(sabrina)
#
# sabrina.level = 2
# print(sabrina)
#
# sabrina.level += 5
# print(sabrina)
#
# # testing decorators
# sabrina.score = 500
# print(sabrina)