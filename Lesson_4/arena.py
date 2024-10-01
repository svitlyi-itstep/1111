from Lesson_2.character import Character
from Lesson_3.paladin import Paladin
from Lesson_3.berserk import Berserk

class Arena:
    players = []

    def __init__(self, players=()):
        for player in players:
            self.players.append(player)


    def add_player(self):
        player_name = input('Введіть ім\'я гравця: ')
        player_health = input('Введіть кількість здоров\'я гравця: ')
        player_damage = input('Введіть кількість шкоди гравця: ')
        player_defence = input('Введіть кількість захисту гравця: ')
        player_class = input('Введіть клас: ').lower()

        if player_class == "paladin":
            self.players.append(Paladin(player_name, player_health,
                                        player_damage, player_defence))
        elif player_class == "berserk":
            self.players.append(Berserk(player_name, player_health,
                                        player_damage, player_defence))
        else:
            self.players.append(Character(player_name, player_health,
                                        player_damage, player_defence))

