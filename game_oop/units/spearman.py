from game_oop.units.infantry import Infantry


class Spearman(Infantry):

    def __init__(self, name: str, team_side: bool):
        super().__init__("Копейщик", 100, name, team_side, 100, (12, 24), 8)
