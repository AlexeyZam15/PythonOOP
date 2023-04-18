from abc import ABC, abstractmethod

from game_oop.coords import Coords


class BaseHero(ABC):

    @abstractmethod
    def __init__(self, class_name: str, hp: int, name: str, team_side: bool, armor: int, damage: tuple,
                 initiative: int) -> object:
        self.__class_name = class_name
        self.__hp = hp
        self.__name = name
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

    def get_hp(self):
        return self.__hp

    def get_name(self):
        return self.__name

    @property
    def class_name(self):
        return self.__class_name
