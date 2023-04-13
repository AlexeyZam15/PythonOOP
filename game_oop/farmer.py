from game_oop.baseHero import BaseHero


class Farmer(BaseHero):

    def __init__(self, name: str):
        BaseHero.__init__(self, "Фермер", 100, name, 100, (8, 10), 10)
