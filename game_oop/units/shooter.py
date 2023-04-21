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
        dmg = randint(self.damage[0], self.damage[1])
        self.log(self.get_info() + " стреляет в " + enemy.get_info())
        enemy.get_damage(dmg)

    def step(self, dark_team, holy_team):
        enemy_team = self.get_enemy_team(dark_team, holy_team).filter_visible_team()
        if self.cant_turn(enemy_team):
            return
        self.turn_begin()
        ally_team = self.get_ally_team(dark_team, holy_team)
        if ally_team.has_live_ally("Фермер") and self.__arrows != self.__max_arrows:
            self.__arrows += 1
            peasant = ally_team.get_live_ally("Фермер")
            peasant.state = "Busy"
            self.log(f'{self.get_info()} берёт стрелу от {peasant.get_info()}')
        if self.__arrows >= 1:
            closest_hero = self.find_closest_hero(enemy_team)
            # print(closest_hero.state)
            self.shoot(closest_hero)
        else:
            self.log(f'{self.get_info()} берёт стрелу со склада')
            self.__arrows += 1
