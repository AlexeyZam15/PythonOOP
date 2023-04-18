from abc import ABC

from game_oop.units.baseHero import BaseHero


class Shooter(BaseHero, ABC):
    def __init__(self, class_name: str, hp: int, name: str, team_side: bool, armor: int, damage: tuple,
                 initiative: int):
        super().__init__(class_name, hp, name, team_side, armor, damage, initiative)
        self.__arrows = 10

    def __str__(self):
        return super().__str__().replace("Статус", "➶: " + str(self.__arrows) + " Статус")
