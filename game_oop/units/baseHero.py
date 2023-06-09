from abc import ABC, abstractmethod

from game_oop.aux_modules.coords import Coords


class BaseHero(ABC):

    @abstractmethod
    def __init__(self, class_name: str, hp: int, name: str, team_side: bool, armor: int, damage: tuple,
                 initiative: int):
        self.__armor_buff = 0
        self.__initiative_buff = 0
        self.__class_name = class_name
        self.__hp = hp
        self.__max_hp = hp
        self.__name = name
        self.__team_side = team_side
        self.__armor = armor
        self.__damage = damage
        self.__initiative = initiative
        self.__state = "Stand"
        self.__position = Coords(team_side)

    def __str__(self):
        return f'{self.__class_name[0]} {self.__name} 💗: {self.__hp} 🛡️: {self.__armor} ' \
               f'🎿: {self.__initiative} ⚔️: {self.__damage[0]} - {self.__damage[1]} ' \
               f'Статус: {self.__state.replace("Dead", "💀").replace("Stand", "🙂")} ' \
               f'{self.__position}'

    @property
    def position(self):
        return self.__position

    @property
    def hp(self):
        return self.__hp

    @property
    def max_hp(self):
        return self.__max_hp

    @property
    def name(self):
        return self.__name

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, string):
        self.__state = string

    @property
    def class_name(self):
        return self.__class_name

    def get_info(self):
        return f'{self.__class_name} {self.__name}'

    @staticmethod
    def log(text: str):
        with open("actions_log.txt", "a", encoding="utf-8") as file:
            file.write(text + "\n")

    def get_damage(self, damage: int):
        if damage > 0:
            self.log(self.get_info() + f" получает {damage} урона")
        else:
            if self.__hp - damage > self.__max_hp:
                damage -= (self.__max_hp - (self.__hp - damage))
            self.log(self.get_info() + f" восстанавливает {-damage} здоровья")
        if self.__armor > 0:
            self.__armor -= damage
            if self.__armor >= 0:
                return
            else:
                damage = abs(self.__armor)
                self.__armor = 0
        if self.__hp - damage > 0:
            self.__hp -= damage
        else:
            self.__hp = 0
            self.__state = "Dead"
            self.log(self.get_info() + " умирает")

    def turn_begin(self):
        if self.__state == "Dead":
            return
        text = "Ходит " + self.get_info()
        if self.__team_side:
            text += " из второй команды"
        else:
            text += " из первой команды"
        self.log(text)

    @abstractmethod
    def step(self, dark_team, holy_team):
        return

    def cant_turn(self, enemy_team):
        if self.state == "Dead":
            return True
        if enemy_team:
            return False
        return True

    def get_ally_team(self, dark_team, holy_team):
        if self.__team_side:
            return holy_team
        return dark_team

    def get_enemy_team(self, dark_team, holy_team):
        if self.__team_side:
            # for hero in dark_team:
            #     print(hero)
            return dark_team
        return holy_team

    @property
    def initiative(self):
        return self.__initiative

    @initiative.setter
    def initiative(self, value):
        self.__initiative = value

    def get_closest_hero(self, team):
        closest_hero = team[0]
        distance = self.position.get_distance(closest_hero.position)
        min_distance = distance
        for i in range(1, len(team)):
            distance = self.position.get_distance(team[i].position)
            if distance < min_distance:
                min_distance = distance
                closest_hero = team[i]
        # print(self.get_info(), min_distance, closest_hero.get_info())
        return closest_hero

    @property
    def damage(self):
        return self.__damage

    @property
    def initiative_buff(self):
        return self.__initiative_buff

    @initiative_buff.setter
    def initiative_buff(self, value):
        self.__initiative_buff = value

    def reset_buffs(self):
        self.__initiative -= self.__initiative_buff
        self.__initiative_buff = 0
        if self.__armor - self.__armor_buff >= 0:
            self.__armor -= self.__armor_buff
        else:
            self.__armor = 0
            self.__armor_buff = 0

    @property
    def hp_diff(self):
        return self.__max_hp - self.__hp

    @property
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, value):
        self.__armor = value

    @property
    def armor_buff(self):
        return self.__armor_buff

    @armor_buff.setter
    def armor_buff(self, value):
        self.__armor_buff = value

    @property
    def team_side(self):
        return self.__team_side
