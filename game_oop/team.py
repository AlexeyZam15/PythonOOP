from game_oop.baseHero import BaseHero
from game_oop.farmer import Farmer
from random import randint

from game_oop.names import Names


class Team:
    all_team = list()
    count = 0

    def __init__(self):
        self.__heroes = list()
        self._current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < len(self.__heroes):
            hero = self.__heroes[self._current_index]
            self._current_index += 1
            return hero
        raise StopIteration

    def append(self, hero: BaseHero):
        self.__heroes.append(hero)
        Team.all_team.append(hero)
        Team.count += 1