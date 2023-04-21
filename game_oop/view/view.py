from game_oop.view.ansiColors import AnsiColors

class View:
    @staticmethod
    def format_div(string: str):
        return string.replace('a', '\u250c') \
            .replace('b', '\u252c') \
            .replace('c', '\u2510') \
            .replace('d', '\u251c') \
            .replace('e', '\u253c') \
            .replace('f', '\u2524') \
            .replace('g', '\u2514') \
            .replace('h', '\u2534') \
            .replace('i', '\u2518') \
            .replace('-', '\u2500')

    @staticmethod
    def tab_setter(cnt: int, max: int):
        dif = max - cnt + 2
        if dif > 2:
            print(" " * dif + ":", end="")
        else:
            print(":\t", end="")

    @staticmethod
    def get_char(y: int, x: int, all_team, dark_team, holy_team):
        out = "| "
        for human in all_team:
            if human.position.equal_coords(x, y):
                if human.hp != 0:
                    if holy_team.__contains__(human):
                        out = "|" + AnsiColors.ANSI_BLUE + human.class_name[0] + AnsiColors.ANSI_RESET
                        break
                    elif dark_team.__contains__(human):
                        out = "|" + (AnsiColors.ANSI_GREEN + human.class_name[0] + AnsiColors.ANSI_RESET)
                        break
                else:
                    out = "|" + (AnsiColors.ANSI_RED + human.class_name[0] + AnsiColors.ANSI_RESET)
                    break
        return out

    @staticmethod
    def view(all_team, dark_team, holy_team):

        step = 1
        l = list({0})
        top_10 = View.format_div("a") + (View.format_div("-b") + View.format_div("-c")) * 5
        middle_10 = View.format_div("d") + (View.format_div("-e") + View.format_div("-f")) * 5
        bottom_10 = View.format_div("g") + (View.format_div("-h") + View.format_div("-i")) * 5

        if step == 1:
            print(AnsiColors.ANSI_RED + "First step" + AnsiColors.ANSI_RESET, end="")
        else:
            print(AnsiColors.ANSI_RED + "step: " + str(step) + AnsiColors.ANSI_RESET, end="")
        step += 1
        l[0] = max([max(l[0], len(str(v))) for v in all_team])
        print("_" * l[0] * 2, end="\n")
        print(top_10 + "    ", end="")
        print(AnsiColors.ANSI_BLUE + "Blue side" + AnsiColors.ANSI_RESET, end="")
        print(" " * (l[0] - 9), end="")
        print(AnsiColors.ANSI_GREEN + " \tGreen side" + AnsiColors.ANSI_RESET, end="\n")
        for i in range(1, 11):
            print(View.get_char(1, i, all_team, dark_team, holy_team), end="")
        print("|    ", end="")
        print(holy_team[0], end="")
        View.tab_setter(len(str(holy_team[0])), l[0])
        print(dark_team[0], end="\n")
        print(middle_10, end="\n")

        for i in range(2, 10):
            for j in range(1, 11):
                print(View.get_char(i, j, all_team, dark_team, holy_team), end="")
            print("|    ", end="")
            print(holy_team[i - 1], end="")
            View.tab_setter(len(str(holy_team[i - 1])), l[0])
            print(dark_team[i - 1], end="\n")
            print(middle_10, end="\n")
        for j in range(1, 11):
            print(View.get_char(10, j, all_team, dark_team, holy_team), end="")
        print("|    ", end="")
        print(holy_team[9], end="")
        View.tab_setter(len(str(holy_team[9])), l[0])
        print(dark_team[9], end="\n")
        print(bottom_10, end="\n")
