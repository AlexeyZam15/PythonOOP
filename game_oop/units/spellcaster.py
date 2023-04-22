from abc import ABC, abstractmethod

from game_oop.units.baseHero import BaseHero


class Spellcaster(BaseHero, ABC):

    @abstractmethod
    def __init__(self, class_name: str, hp: int, name: str, team_side: bool, armor: int, damage: tuple,
                 initiative: int, mana: int):
        super().__init__(class_name, hp, name, team_side, armor, damage, initiative)
        self.__mana = mana
        self.__max_mana = mana

    @abstractmethod
    def cast_spell(self, ally_team, enemy_team):
        pass

    @property
    def small_spell_cost(self):
        return 10

    @property
    def big_spell_cost(self):
        return 30

    def step(self, dark_team, holy_team):
        enemy_team = self.get_enemy_team(dark_team, holy_team).filter_visible_team()
        if self.cant_turn(enemy_team):
            return
        self.turn_begin()
        ally_team = self.get_ally_team(dark_team, holy_team)
        if ally_team.has_live_ally("Фермер") and self.__mana + 25 < self.__max_mana:
            self.__mana += 25
            peasant = ally_team.get_live_ally("Фермер")
            peasant.state = "Busy"
            self.log(f'{self.get_info()} берёт зелье маны от {peasant.get_info()}')
        if self.__mana >= self.small_spell_cost:
            self.cast_spell(ally_team, enemy_team)
        else:
            self.log(f'{self.get_info()} берёт зелье маны со склада')
            self.__mana += 25

    def __str__(self):
        return super().__str__().replace("Статус", "💧: " + str(self.__mana) + " Статус")

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, value):
        self.__mana = value
