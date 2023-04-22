from game_oop.units.shooter import Shooter


class Crossbowman(Shooter):
    def __init__(self, name: str, team_side: bool):
        super().__init__("Арбалетчик", 50, name, team_side, 30, (10, 20), 9)
