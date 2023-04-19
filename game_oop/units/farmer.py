from game_oop.units.baseHero import BaseHero


class Farmer(BaseHero):

    def __init__(self, name: str, team_side):
        super().__init__("Фермер", 100, name, team_side, 100, (8, 10), 1)

    def step(self, dark_team, holy_team):
        if self.cant_turn(self.get_enemy_team(dark_team, holy_team)):
            return
        self.turn_begin()
        if self.state == "Busy":
            self.log(self.get_info() + " пополнил запасы")
            self.state = "Stand"
