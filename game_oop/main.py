from team import Team
from game_oop.farmer import Farmer
from names import Names
from random import randint


def fill_team(team: Team, size: int, cls: list, team_side):
    for i in range(size):
        team.append(cls[randint(0, len(cls) - 1)](Names.get_random_name(), team_side))


classes = list({Farmer})

holy_team = Team()
fill_team(holy_team, 10, classes, True)
dark_team = Team()
fill_team(dark_team, 10, classes, False)

print(*holy_team, sep="\n")

print()

print(*dark_team, sep="\n")

print()

# print(*Team.all_team, sep="\n")
#
# print(Team.count)

# list(map(lambda x: x.__get_ally_team(), BaseHero.get_dark_team()))
