from abc import ABC
from random import randint

from game_oop.units.baseHero import BaseHero


class Shooter(BaseHero, ABC):
    def __init__(self, class_name: str, hp: int, name: str, team_side: bool, armor: int, damage: tuple,
                 initiative: int):
        super().__init__(class_name, hp, name, team_side, armor, damage, initiative)
        self.__arrows = 10
        self.__max_arrows = 10

    def __str__(self):
        return super().__str__().replace("Статус", "➶: " + str(self.__arrows) + " Статус")

    def shoot(self, enemy: BaseHero):
        self.__arrows -= 1
        dmg = randint(self.__damage[0], self.__damage[1])
        self.log(self.get_info() + " стреляет в " + enemy.get_info())
        enemy.get_damage(dmg)

    def step(self, dark_team, holy_team):
        if self.cant_turn(self.get_enemy_team(dark_team, holy_team)):
            return
        self.turn_begin()
