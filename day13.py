# find all possible paths to prize
# get one with least tokens
# add to total tokens

with open("day13.txt") as f:
    prizes = f.readlines()

for i in range(len(prizes)):
    if i != len(prizes) - 1:
        prizes[i] = prizes[i][:-1]

claw_machines = [[[int(prizes[n + m].split(': ')[1].split(', ')[p][2:]) for p in range(2)] for m in range(3)] for n in range(0, len(prizes), 4)]
tokens = 0

for n in range(len(claw_machines)):
    for p in range(2):
        claw_machines[n][2][p] += 10000000000000

for machine in claw_machines:
    token = 0
    ftoken = 0
    n = int(machine[2][0] / machine[0][0]) + 1
    x = n * machine[0][0]
    y = n * machine[0][1]
    token = n * 3
    while n > 0:
        if (x, y) == (machine[2][0], machine[2][1]):
            if token < ftoken or ftoken == 0:
                ftoken = token
        if x >= machine[2][0] or y >= machine[2][1]:
            x -= machine[0][0]
            y -= machine[0][1]
            token -= 3
            n -= 1
        if x < machine[2][0] and y < machine[2][1]:
            x += machine[1][0]
            y += machine[1][1]
            token += 1
    tokens += ftoken

print(tokens)