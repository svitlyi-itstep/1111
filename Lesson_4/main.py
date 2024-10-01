from Lesson_2.character import Character
from Lesson_3.paladin import Paladin
from Lesson_3.berserk import Berserk

players_list = []

player_1_name = input('Введіть ім\'я першого гравця: ')
player_1_class = input('Введіть клас: ').lower()

if player_1_class == "paladin":
    player1 = Paladin(player_1_name, 100, 15, 0)
elif player_1_class == "berserk":
    player1 = Berserk(player_1_name, 100, 15, 0)
else:
    player1 = Character(player_1_name, 100, 15, 0)

print(player1)
players_list.append(player1)

player2 = Paladin("Petya", 100, 20, 4)
player2.show_stats()

while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    player2.attack(player1)

    print(f"\n{player1}\n{player2}\n")

