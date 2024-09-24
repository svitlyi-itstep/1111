from Lesson_2.character import Character
from paladin import Paladin

player1 = Character("Vasya", 100, 10, 0)
print(player1)

player2 = Paladin("Petya", 100, 3, 4)
player2.show_stats()

player1.attack(player2)
player2.attack(player1)

print(f"\n{player1}\n{player2}\n")