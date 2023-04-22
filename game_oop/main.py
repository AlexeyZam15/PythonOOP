from game_oop.units.bowman import Bowman
from game_oop.units.crossbowman import Crossbowman
from game_oop.units.wizard import Wizard
from game_oop.view.view import View
from team import Team
from game_oop.units.farmer import Farmer


def main():
    classes = list({Farmer, Bowman, Crossbowman, Wizard})

    holy_team = Team()
    dark_team = Team()
    Team.fill_teams(dark_team, holy_team, 10, classes)
    all_team = Team.all_team
    string = ""
    view_o = View()
    step = 1
    with open("actions_log.txt", "w", encoding="utf-8") as file:
        file.write("")
    while string != "q":
        view_o.view(all_team, dark_team, holy_team)
        string = input("Нажмите enter для продолжения или введите q для выхода\n")
        with open("actions_log.txt", "a", encoding="utf-8") as file:
            file.write("_"*60 + f"\nstep {step}\n" + "_"*60 + "\n")
        step += 1
        initiative_list = sorted(all_team, key=lambda h: h.initiative, reverse=True)
        for hero in initiative_list:
            hero.step(dark_team, holy_team)


if __name__ == "__main__":
    main()
