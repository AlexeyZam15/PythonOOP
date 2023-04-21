from game_oop.units.bowman import Bowman
from game_oop.view.view import View
from team import Team
from game_oop.units.farmer import Farmer


def main():
    classes = list({Farmer, Bowman})

    holy_team = Team()
    dark_team = Team()
    Team.fill_teams(dark_team, holy_team, 10, classes)
    all_team = Team.all_team
    string = ""
    with open("actions_log.txt", "w", encoding="utf-8") as file:
        file.write("")
    while string != "q":
        View.view(all_team, dark_team, holy_team)
        string = input("Нажмите enter для продолжения или введите q для выхода")
        initiative_list = sorted(all_team.copy(), key=lambda h: h.initiative, reverse=True)
        for hero in initiative_list:
            hero.step(dark_team, holy_team)


if __name__ == "__main__":
    main()
