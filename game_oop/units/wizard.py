from random import randint

from game_oop.units.spellcaster import Spellcaster


class Wizard(Spellcaster):

    def __init__(self, name: str, team_side: bool):
        super().__init__("Волшебник", 50, name, team_side, 0, (2, 4), 6, 40)

    def cast_spell(self, ally_team, enemy_team):
        closest_enemy = self.find_closest_hero(enemy_team)
        if self.mana >= self.big_spell_cost:
            self.cast_fireball(closest_enemy)
        else:
            self.cast_acceleration(closest_enemy.find_closest_hero(ally_team))

    def cast_fireball(self, enemy):
        self.mana -= self.big_spell_cost
        self.log(f'{self.get_info()} применяет заклинание Фаербол на {enemy.get_info()}')
        enemy.get_damage(randint(15, 31))
        pass

    def cast_acceleration(self, ally):
        self.mana -= self.small_spell_cost
        ally.initiative += 2
        ally.initiative_buff += 2
        self.log(f'{self.get_info()} применяет заклинание Ускорение на {ally.get_info()}')
