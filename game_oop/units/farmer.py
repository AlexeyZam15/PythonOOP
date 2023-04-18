from game_oop.units.baseHero import BaseHero


class Farmer(BaseHero):

    def __init__(self, name: str, team_side):
        super().__init__("Фермер", 100, name, team_side, 100, (8, 10), 1)
