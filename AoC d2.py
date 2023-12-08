# %%
f = open("input2.txt", "r")

def part1(f):
    cube_limits = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    possible_ids = []

    for line in f:
        elements = line.split(': ')

        game_id = int(elements[0].split(' ')[1])
        impossible = False

        for game_set in elements[1].strip().split('; '):
            cubes = game_set.split(', ')
            for cube in cubes:
                quantity, color = cube.split(' ')

                if(cube_limits[color] < int(quantity)):
                    impossible = True
                    break
            
            if(impossible):
                break

        if(not impossible):
            possible_ids.append(game_id)

    return sum(possible_ids)



# %%
import math
f = open("input2.txt", "r")

powers = []

for line in f:
    elements = line.split(': ')
    minimum_cubes = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for game_set in elements[1].strip().split('; '):
        cubes = game_set.split(', ')
        for cube in cubes:
            quantity, color = cube.split(' ')

            minimum_cubes[color] = max(int(quantity), minimum_cubes[color])

    powers.append(math.prod(minimum_cubes.values()))
        

print(sum(powers))
# %%
