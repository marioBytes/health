import random

'''
In this program the health variable represents the start health of a
player in a video game. Depending on the difficulty of the game (1 =
easy, 2 = medium, and 3 = hard), the health potion (potion_health
variable) that the player aquires will be a random number generated
between 25 and 50, which will be divided by the difficulty of the
game, and will thus be added to the players health.
'''

health = 50

difficulty = 1

potion_health = int(random.randint(25, 50) /difficulty)

health = health + potion_health
print(health)

