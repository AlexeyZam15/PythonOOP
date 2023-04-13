from baseHero import BaseHero
from names import Names

for i in range(10):
    hero1 = BaseHero("Герой", 100, Names.get_random_name(), True, 100, (8, 10), 10)

print(*BaseHero.get_holy_team(), sep="\n")
print(BaseHero.get_count())

for i in range(10):
    BaseHero("Герой", 100, Names.get_random_name(), False, 100, (8, 10), 10)
print(*BaseHero.get_dark_team(), sep="\n")
print(BaseHero.get_count())
