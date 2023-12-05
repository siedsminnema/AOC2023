from collections import defaultdict

from input import get_input

almanac = get_input(5)

seeds = almanac[0].split()[1:]

maps = defaultdict(list)
mapnames = []

for line in almanac[2:]:
    print(line)
    if "map" in line:
        current_name = line
        mapnames.append(line)
    elif line != '':
        dr, sr, rl = line.split()
        maps[current_name].append([int(dr), int(sr), int(rl)])

locations = []
for seed in seeds:
    current = int(seed)
    for mapname in mapnames:
        for instruction in maps[mapname]:
            print("!!!!!", current, instruction, mapname)
            if instruction[1] <= current <= instruction[1] + instruction[2]:
                current += (instruction[0] - instruction[1])
                print("instruction found", current)
                break
        if "location" in mapname:
            locations.append(current)
            print("yes!")

print(locations)
print(min(locations))




