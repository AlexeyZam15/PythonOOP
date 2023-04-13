from datetime import datetime as dt


class Player:
    __LVL, __HEALTH = 1, 100
    # разрешённые свойства экземпляра
    __slots__ = ['__lvl', '__health', '__born']

    def __init__(self):
        self.__lvl = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = dt.now()

    # @ - декораторы
    # геттер
    # def get_lvl(team_side):
    #     return team_side.__lvl
    @property
    def lvl(self):
        return self.__lvl, f'{dt.now() - self.__born}'

    # сеттер
    # def set_lvl(team_side, numeric):
    #     team_side.__lvl += numeric
    @lvl.setter
    def lvl(self, numeric):
        self.__lvl += Player.__type_test(numeric)
        if self.__lvl >= 100:
            self.__lvl = 100

    @classmethod
    def set_cls_field(cls, lvl=1, health=100):
        cls.__LVL = Player.__type_test(lvl)
        cls.__HEALTH = Player.__type_test(health)

    @staticmethod
    def __type_test(value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError('Must be int')

# x = Player()
#
# # print(x.get_lvl())
# # print(x.set_lvl(2))
# # print(print(x.get_lvl()))
# print(x.lvl)
# x.lvl = 5
# print(x.lvl)
