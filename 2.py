from input import get_input

games = get_input(2)

list_of_fail_games = []
all_games = []

for game in games:
    n, game = game.split(':')
    all_games.append(n)
    for subgame in game.split(';'):
        for reveal in subgame.split(','):
            value, color = reveal.split()
            if color == "red" and int(value) > 12:
                list_of_fail_games.append(n)
            if color == "green" and int(value) > 13:
                list_of_fail_games.append(n)
            if color == "blue" and int(value) > 14:
                list_of_fail_games.append(n)

part_1 = 0
good_games = set(all_games) - set(list_of_fail_games)
for g in good_games:
    v = g.split()[1]
    part_1 += int(v)

print(part_1)
powers = []
for game in games:
    n, game = game.split(':')
    f_blue, f_red, f_green = 0, 0, 0
    for subgame in game.split(';'):
        for reveal in subgame.split(','):
            value, color = reveal.split()
            if color == "red" and int(value) > f_red:
                f_red = int(value)
            if color == "green" and int(value) > f_green:
                f_green = int(value)
            if color == "blue" and int(value) > f_blue:
                f_blue = int(value)
    powers.append(f_red * f_green * f_blue)
print(sum(powers))