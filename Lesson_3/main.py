from Lesson_2.character import Character
from paladin import Paladin
from berserk import Berserk

player1 = Berserk("Vasya", 100, 15, 0)
print(player1)

player2 = Paladin("Petya", 100, 20, 4)
player2.show_stats()

while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    player2.attack(player1)

    print(f"\n{player1}\n{player2}\n")