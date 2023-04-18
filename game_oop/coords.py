class Coords:
    __last_first_team_x = 1
    __last_first_team_y = 1
    __last_second_team_x = 10
    __last_second_team_y = 1

    def __init__(self, team_side: bool):
        if team_side:
            self.x = Coords.__last_first_team_x
            self.y = Coords.__last_first_team_y
            Coords.__last_first_team_y += 1
        else:
            self.x = Coords.__last_second_team_x
            self.y = Coords.__last_second_team_y
            Coords.__last_second_team_y += 1
