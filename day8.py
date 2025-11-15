# find antinodes
# check if in the ranges
# add to set

with open("day8.txt") as f:
    l = f.readlines()

antinodes = set()
antennae = {}

for n in range(len(l)):
    for m in range(len(l[0]) - 1):
        if l[n][m].isalpha() or l[n][m].isnumeric():
            if l[n][m] in antennae:
                antennae[l[n][m]].append((n, m))
            else:
                antennae[l[n][m]] = [(n, m)]

print(antennae)

for antenna in antennae:
    for i in range(len(antennae[antenna])):
        for a in antennae[antenna][:i] + antennae[antenna][i + 1:]:
            for n in range(100):
                if 0 <= antennae[antenna][i][0] + (antennae[antenna][i][0] - a[0]) * n <= len(l) - 1 and 0 <= antennae[antenna][i][1] + (antennae[antenna][i][1] - a[1]) * n <= len(l[0]) - 2:
                    antinodes.add((antennae[antenna][i][0] + (antennae[antenna][i][0] - a[0]) * n, antennae[antenna][i][1] + (antennae[antenna][i][1] - a[1]) * n))

print(antinodes)
print(len(antinodes))