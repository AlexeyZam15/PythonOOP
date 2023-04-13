from game_oop.baseHero import BaseHero


class Farmer(BaseHero):

    def __init__(self, name: str, team_side):
        BaseHero.__init__(self, "Фермер", 100, name, team_side, 100, (8, 10), 10)
