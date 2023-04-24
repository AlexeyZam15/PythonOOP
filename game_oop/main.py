from game_oop.units.bowman import Bowman
from game_oop.units.crossbowman import Crossbowman
from game_oop.units.monk import Monk
from game_oop.units.rogue import Rogue
from game_oop.units.spearman import Spearman
from game_oop.units.wizard import Wizard
from game_oop.view.view import View
from game_oop.aux_modules.team import Team
from game_oop.units.farmer import Farmer


def game_ended(dark_team, holy_team):
    if dark_team.filter_live() and holy_team.filter_live():
        return False
    return True


def print_win(dark_team):
    if dark_team.filter_live():
        print("Все персонажи в первой команде мертвы\nПобедила вторая команда")
    else:
        print("Все персонажи во второй команде мертвы\nПобедила первая команда")


def main():
    classes = list({Farmer, Bowman, Crossbowman, Wizard, Monk, Spearman, Rogue})

    holy_team = Team()
    dark_team = Team()
    Team.fill_teams(dark_team, holy_team, 10, classes)
    all_team = holy_team + dark_team
    string = ""
    view_o = View()
    step = 1
    view_o.view(all_team, dark_team, holy_team)
    while string != "q" and game_ended(dark_team, holy_team) is False:
        string = input("Нажмите enter для продолжения или введите q для выхода\n")
        with open("actions_log.txt", "a", encoding="utf-8") as file:
            file.write("_" * 60 + f"\nstep {step}\n" + "_" * 60 + "\n")
        step += 1
        initiative_list = sorted(all_team, key=lambda h: h.initiative, reverse=True)
        for hero in initiative_list:
            hero.step(dark_team, holy_team)
        view_o.view(all_team, dark_team, holy_team)
    if game_ended(dark_team, holy_team):
        print_win(dark_team)


if __name__ == "__main__":
    with open("actions_log.txt", "w", encoding="utf-8") as file:
        file.write("")
    main()
