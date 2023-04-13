class BaseHero:
    __count = 0
    __holy_team = list()
    __dark_team = list()
    __all_team = list()

    def __init__(self, class_name: str, hp: int, name: str, team: bool, armor: int, damage: tuple, initiative: int):
        self.__class_name = class_name
        self.__hp = hp
        self.__name = name
        self.__team = team
        self.__armor = armor
        self.__damage = damage
        self.__initiative = initiative
        self.__status = "Stand"
        self.__get_ally_team().append(self)
        BaseHero.__count += 1

    def __str__(self):
        return self.__class_name[0] + " " + self.__name + " " + str(self.__hp) + " " + str(self.__armor) \
            + " " + (str(self.__damage)) + " " + self.__status

    @classmethod
    def get_count(cls):
        return cls.__count

    @classmethod
    def get_holy_team(cls):
        return cls.__holy_team

    @classmethod
    def get_dark_team(cls):
        return cls.__dark_team

    def __get_ally_team(self):
        return self.__holy_team if self.__team else self.__dark_team

    # def __getitem__(self, item):
    #     return self.marks[item]





