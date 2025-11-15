# make the guard move
# replace spaces with X's
# count X's

with open("day6.txt") as f:
    l = f.readlines()

for i in range(len(l)):
    l[i] = list(l[i])

guards = ['^', '>', 'v', '<']
coords = [59, 70]
turn_points = []
path_points = []
infinite_points = []
face = 0
sum = 0
board = ''

while True:
    if coords[0] == 0 or coords[0] == len(l) - 1 or coords[1] == 0 or coords[1] == len(l[0]) - 2:
        l[coords[0]][coords[1]] = 'X'
        break
    elif (face % 4 == 0 and l[coords[0] - 1][coords[1]] == '#') or (face % 4 == 1 and l[coords[0]][coords[1] + 1] == '#') or (face % 4 == 2 and l[coords[0] + 1][coords[1]] == '#') or (face % 4 == 3 and l[coords[0]][coords[1] - 1] == '#'):
        if coords in turn_points:
            sum += 1
            break
        else:
            turn_points.append([coords[0], coords[1]])
            face += 1

    l[coords[0]][coords[1]] = 'X'

    if face % 4 == 0:
        coords[0] -= 1
    elif face % 4 == 1:
        coords[1] += 1
    elif face % 4 == 2:
        coords[0] += 1
    else:
        coords[1] -= 1

    l[coords[0]][coords[1]] = guards[face % 4]

for n in range(len(l)):
    for m in range(len(l[0]) - 1):
        if l[n][m] == 'X':
            path_points.append([n, m])

coords = [59, 70]
turn_points = []
face = 0

with open("day6.txt") as f:
    l = f.readlines()

for i in range(len(l)):
    l[i] = list(l[i])

for p in path_points:
    if l[p[0]][p[1]] == '.':
        l[p[0]][p[1]] = '#'
        while True:
            if coords[0] == 0 or coords[0] == len(l) - 1 or coords[1] == 0 or coords[1] == len(l[0]) - 2:
                l[coords[0]][coords[1]] = 'X'
                break
            elif (face % 4 == 0 and l[coords[0] - 1][coords[1]] == '#') or (face % 4 == 1 and l[coords[0]][coords[1] + 1] == '#') or (face % 4 == 2 and l[coords[0] + 1][coords[1]] == '#') or (face % 4 == 3 and l[coords[0]][coords[1] - 1] == '#'):
                if coords in turn_points:
                    sum += 1
                    break
                else:
                    turn_points.append([coords[0], coords[1]])
                    face += 1

            l[coords[0]][coords[1]] = 'X'

            if face % 4 == 0:
                coords[0] -= 1
            elif face % 4 == 1:
                coords[1] += 1
            elif face % 4 == 2:
                coords[0] += 1
            else:
                coords[1] -= 1
    
            l[coords[0]][coords[1]] = guards[face % 4]

        coords = [59, 70]
        turn_points = []
        face = 0

        with open("day6.txt") as f:
            l = f.readlines()

        for i in range(len(l)):
            l[i] = list(l[i])

print(path_points)
print(len(path_points))
print(sum)