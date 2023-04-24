from game_oop.units.infantry import Infantry


class Spearman(Infantry):

    def __init__(self, name: str, team_side: bool):
        super().__init__("Копейщик", 100, name, team_side, 100, (12, 24), 8)

    def step(self, dark_team, holy_team):
        if self.cant_turn(self.get_enemy_team(dark_team, holy_team).filter_visible()):
            return
        self.turn_begin()
        super().step(dark_team, holy_team)
