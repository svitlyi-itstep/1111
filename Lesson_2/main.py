from character import Character

player1 = Character("Vasya", 100, 105, 0)
print(player1)

player2 = Character("Petya", 100, 3, 2)
player2.show_stats()

player1.attack(player2)

print(f"\n{player1}\n{player2}\n")