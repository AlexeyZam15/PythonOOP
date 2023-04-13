from baseHero import BaseHero
from team import Team
from game_oop.farmer import Farmer
from names import Names

holy_team = Team()
dark_team = Team()

for i in range(1, 11):
    holy_team.append(Farmer(Names.get_random_name()))

print(*holy_team, sep="\n")

for i in range(1, 11):
    dark_team.append(Farmer(Names.get_random_name()))

print()

print(*dark_team, sep="\n")

print()

print(*Team.all_team, sep="\n")

print(Team.count)

# list(map(lambda x: x.__get_ally_team(), BaseHero.get_dark_team()))
