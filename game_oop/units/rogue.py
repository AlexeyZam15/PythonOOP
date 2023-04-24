from game_oop.units.infantry import Infantry


class Rogue(Infantry):

    def __init__(self, name: str, team_side: bool):
        super().__init__("Разбойник", 50, name, team_side, 30, (9, 29), 15)

    @staticmethod
    def filter_visible_special(enemy_team):
        return enemy_team.filter_visible_rogue()

    def step(self, dark_team, holy_team):
        if self.cant_turn(self.filter_visible_special(self.get_enemy_team(dark_team, holy_team))):
            return
        self.turn_begin()

        if self.state != "Hide":
            self.state = "Hide"
            self.log(f'{self.get_info()} прячется')
        else:
            self.state = "Stand"
            self.log(f'{self.get_info()} раскрылся')

        super().step(dark_team, holy_team)

    def __str__(self):
        return super().__str__().replace("Hide", u'\U0001f400')
