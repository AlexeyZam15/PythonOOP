from abc import ABC, abstractmethod
from random import randint

from game_oop.units.baseHero import BaseHero


class Infantry(BaseHero, ABC):

    @abstractmethod
    def __init__(self, class_name: str, hp: int, name: str, team_side: bool, armor: int, damage: tuple,
                 initiative: int):
        super().__init__(class_name, hp, name, team_side, armor, damage, initiative)

    def attack(self, enemy: BaseHero):
        self.log(f'{self.get_info()} атакует {enemy.get_info()}')
        enemy.get_damage(randint(self.damage[0], self.damage[1]))

    @staticmethod
    def filter_visible_special(enemy_team):
        return enemy_team.filter_visible()

    def step(self, dark_team, holy_team):

        enemy_team = self.filter_visible_special(self.get_enemy_team(dark_team, holy_team))
        closest_enemy: BaseHero = self.get_closest_hero(enemy_team)
        enemy_position = closest_enemy.position
        my_position = self.position

        distance = my_position.get_distance(closest_enemy.position)
        if distance <= 1:
            self.attack(closest_enemy)
            return

        x_diff = enemy_position.x - my_position.x
        y_diff = enemy_position.y - my_position.y

        move_x = 0
        move_y = 0

        def sign(x):
            return -1 if x < 0 else (1 if x > 0 else 0)

        s_x = sign(x_diff)
        s_y = sign(y_diff)

        if abs(x_diff) > abs(y_diff):
            move_x += s_x
        else:
            move_y += s_y

        flag = True
        ally_team = self.filter_visible_special(self.get_ally_team(dark_team, holy_team))

        if not ally_team.check_position(my_position.x + move_x, my_position.y + move_y):
            move_x = 0
            move_y = 0
            flag = False
            if ally_team.check_position(my_position.x, my_position.y + move_y + s_y):
                move_y = s_y
                flag = True
            elif ally_team.check_position(my_position.x + s_x, my_position.y):
                move_x = s_x
                flag = True

        self.log(f'{self.get_info()} направляется к {closest_enemy.get_info()}')

        my_position.x += move_x
        my_position.y += move_y

        self.reset_buffs()
