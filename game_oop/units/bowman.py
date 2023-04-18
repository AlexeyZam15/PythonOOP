from game_oop.units.shooter import Shooter


class Bowman(Shooter):
    def __init__(self, name: str, team_side: bool):
        super().__init__("Лучник", 50, name, team_side, 10, (8, 16), 10)
