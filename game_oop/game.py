from game_oop.units.bowman import Bowman
from game_oop.units.crossbowman import Crossbowman
from game_oop.units.monk import Monk
from game_oop.units.rogue import Rogue
from game_oop.units.spearman import Spearman
from game_oop.units.wizard import Wizard
from game_oop.view.view import View
from game_oop.aux_modules.team import Team
from game_oop.units.farmer import Farmer


class Game:
    classes = list({Farmer, Bowman, Crossbowman, Wizard, Monk, Spearman, Rogue})

    def __init__(self):
        with open("actions_log.txt", "w", encoding="utf-8") as file:
            file.write("")
        self.__dark_team = Team()
        self.__holy_team = Team()
        self.__all_team = Team()

    def create_teams(self):
        Team.fill_teams(self.__dark_team, self.__holy_team, 10, self.classes)
        self.__all_team = self.__dark_team + self.__holy_team

    def game_ended(self):
        if self.__dark_team.filter_live() and self.__holy_team.filter_live():
            return False
        return True

    def print_win(self):
        if self.__dark_team.filter_live():
            print("Все персонажи в первой команде мертвы\nПобедила вторая команда")
        else:
            print("Все персонажи во второй команде мертвы\nПобедила первая команда")

    @property
    def all_team(self):
        return self.__all_team

    @property
    def dark_team(self):
        return self.__dark_team

    @property
    def holy_team(self):
        return self.__holy_team

    def teams_make_turns(self):
        initiative_list = sorted(self.__all_team, key=lambda h: h.initiative, reverse=True)
        for hero in initiative_list:
            hero.step(self.__dark_team, self.__holy_team)


def main():
    game = Game()
    game.create_teams()

    string = ""
    view_o = View()
    step = 1
    view_o.view(game.all_team, game.dark_team, game.holy_team)
    while string != "q" and game.game_ended() is False:
        string = input("Нажмите enter для продолжения или введите q для выхода\n")
        with open("actions_log.txt", "a", encoding="utf-8") as file:
            file.write("_" * 60 + f"\nstep {step}\n" + "_" * 60 + "\n")
        step += 1
        game.teams_make_turns()
        view_o.view(game.all_team, game.dark_team, game.holy_team)
    if game.game_ended():
        game.print_win()


if __name__ == "__main__":
    main()
