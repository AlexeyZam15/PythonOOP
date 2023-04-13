from abc import ABC, abstractmethod


class BaseHero(ABC):

    @abstractmethod
    def __init__(self, class_name: str, hp: int, name: str, armor: int, damage: tuple, initiative: int) -> object:
        self.__class_name = class_name
        self.__hp = hp
        self.__name = name
        self.__armor = armor
        self.__damage = damage
        self.__initiative = initiative
        self.__status = "Stand"

    def __str__(self):
        return self.__class_name[0] + " " + self.__name + " " + str(self.__hp) + " " + str(self.__armor) \
            + " " + (str(self.__damage)) + " " + self.__status