from random import randint

from game_oop.units.spellcaster import Spellcaster


class Monk(Spellcaster):

    def __init__(self, name: str, team_side: bool):
        super().__init__("Монах", 50, name, team_side, 0, (2, 4), 6, 40)

    def cast_heal(self, enemy):
        self.mana -= self.big_spell_cost
        self.log(f'{self.get_info()} применяет заклинание Исцеление на {enemy.get_info()}')
        enemy.get_damage(-randint(15, 31))
        pass

    def cast_stone_armor(self, ally):
        self.mana -= self.small_spell_cost
        ally.armor += 15
        ally.armor_buff += 15
        self.log(f'{self.get_info()} применяет заклинание Каменный Доспех на {ally.get_info()}')

    def cast_spell(self, ally_team, enemy_team):
        closest_enemy = self.find_closest_hero(enemy_team)
        if self.mana >= self.big_spell_cost and ally_team.has_injured_hero():
            self.cast_heal(ally_team.get_lowest_hp_hero())
        else:
            if ally_team.has_live_ally("Разбойник"):
                self.cast_stone_armor(ally_team.get_live_ally("Разбойник"))
            elif ally_team.has_live_ally("Копейщик"):
                self.cast_stone_armor(ally_team.get_live_ally("Копейщик"))
            else:
                self.cast_stone_armor(closest_enemy.find_closest_hero(ally_team))
