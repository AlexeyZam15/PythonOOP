class Coords:
    __last_first_team_x = 1
    __last_first_team_y = 1
    __last_second_team_x = 10
    __last_second_team_y = 1

    def __init__(self, team_side: bool):
        if team_side:
            self.__x = Coords.__last_first_team_x
            self.__y = Coords.__last_first_team_y
            Coords.__last_first_team_y += 1
        else:
            self.__x = Coords.__last_second_team_x
            self.__y = Coords.__last_second_team_y
            Coords.__last_second_team_y += 1

    def equal_coords(self, x: int, y: int):
        return self.__x == x and self.__y == y

    def __str__(self):
        return f'x: {self.__x} y: {self.__y}'

    def get_distance(self, coords):
        return ((self.__x - coords.__x) ** 2 + (self.__y - coords.__y) ** 2) ** (1 / 2)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
