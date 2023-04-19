from abc import ABC, abstractmethod

from game_oop.coords import Coords
from game_oop.team import Team


class BaseHero(ABC):

    @abstractmethod
    def __init__(self, class_name: str, hp: int, name: str, team_side: bool, armor: int, damage: tuple,
                 initiative: int):
        self.__class_name = class_name
        self.__hp = hp
        self.__name = name
        self.__team_side = team_side
        self.__armor = armor
        self.__damage = damage
        self.__initiative = initiative
        self.__state = "Stand"
        self.__position = Coords(team_side)

    def __str__(self):
        return self.__class_name[0] + " " + self.__name + " 💗: " + str(self.__hp) + " 🛡️: " + str(self.__armor) \
            + " 🎿: " + str(self.__initiative) + " ⚔️: " + (str(self.__damage[0]) + "-" + str(self.__damage[1])) \
            + " Статус: " + self.__state.replace("Dead", "💀").replace("Stand", "🙂") \
            + " x: " + str(self.__position.x) + " y: " + str(self.__position.y)

    def equal_coords(self, x: int, y: int):
        return self.__position.x == x and self.__position.y == y

    @property
    def hp(self):
        return self.__hp

    @property
    def name(self):
        return self.__name

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, string):
        self.__state = string

    @property
    def class_name(self):
        return self.__class_name

    def get_info(self):
        return f'{self.__class_name} {self.__name}'

    @staticmethod
    def log(text: str):
        with open("actions_log.txt", "a", encoding="utf-8") as file:
            file.write(text + "\n")

    def get_damage(self, damage: int):
        if damage > 0:
            self.log(self.get_info() + f" получает {damage} урона")
        else:
            self.log(self.get_info() + f" восстанавливает {-damage} здоровья")
        if self.__armor > 0:
            self.__armor -= damage
            if self.__armor >= 0:
                return
            else:
                damage = abs(self.__armor)
                self.__armor = 0
        if self.__hp - damage > 0:
            self.__hp -= damage
        else:
            self.__hp = 0
            self.__state = "Dead"
            self.log(self.get_info() + " умирает")

    def turn_begin(self):
        if self.__state == "Dead":
            return
        text = "Ходит " + self.get_info()
        if self.__team_side:
            text += " из второй команды"
        else:
            text += " из первой команды"
        self.log(text)

    @abstractmethod
    def step(self, dark_team, holy_team):
        return

    def cant_turn(self, enemy_team):
        # print(enemy_team.size)
        if self.state == "Dead":
            return True
        # visible_team = list(filter(lambda s: s.state == "Stand", enemy_team))
        visible_team = enemy_team.filter_visible_team()
        # print(visible_team.size)
        if visible_team.size == 0:
            return True
        return False

    def get_ally_team(self, dark_team, holy_team):
        if self.__team_side:
            return holy_team
        return dark_team

    def get_enemy_team(self, dark_team, holy_team):
        if self.__team_side:
            # for hero in dark_team:
            #     print(hero)
            return dark_team
        return holy_team

    @property
    def initiative(self):
        return self.__initiative
