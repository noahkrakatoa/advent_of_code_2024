# find all trailheads
# get all paths
# score all trailheads

with open("day10.txt") as f:
    l = f.readlines()

trailheads = []
sum = 0

for n in range(len(l)):
    for m in range(len(l[0]) - 1):
        if l[n][m] == '0':
            trailheads.append([(n, m)])

print(trailheads)

for height in range(1, 10):
    for i in range(len(trailheads)):
        newtrails = []
        for t in trailheads[i]:
            if t[0] > 0 and l[t[0] - 1][t[1]] == str(height):
                newtrails.append((t[0] - 1, t[1]))
            if t[0] < len(l) - 1 and l[t[0] + 1][t[1]] == str(height):
                newtrails.append((t[0] + 1, t[1]))
            if t[1] > 0 and l[t[0]][t[1] - 1] == str(height):
                newtrails.append((t[0], t[1] - 1))
            if t[1] < len(l[0]) - 2 and l[t[0]][t[1] + 1] == str(height):
                newtrails.append((t[0], t[1] + 1))
        trailheads[i] = newtrails

for trail in trailheads:
    sum += len(trail)

print(sum)