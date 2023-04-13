from game_oop.baseHero import BaseHero


class Farmer(BaseHero):
    def __init__(self, hp: int, name: str, armor: int, damage: tuple):
        super().__init__(hp, name, armor, damage)