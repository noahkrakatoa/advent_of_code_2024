# dictionary of all crop coords
# region perimeters and areas calculated simultaneously
# add to total

with open("day12.txt") as f:
    l = f.readlines()

crops = {}
regions = []
i = 0
price = 0

for n in range(len(l)):
    for m in range(len(l[0]) - 1):
        if l[n][m] in crops:
            crops[l[n][m]].append((n, m))
        else:
            crops[l[n][m]] = [(n, m)]

print(crops)

if any([[], [], []]):
    print('hi')

while any([crops[c] for c in crops]):
    for c in crops:
        if crops[c]:
            regions.append([4, 1, 0, [(crops[c][0])]])
            r1, r2 = [], [crops[c].pop(0)]
            while r1 != r2:
                r1 = r2
                r2 = []
                for coords in r1:
                    if (coords[0] - 1, coords[1]) in crops[c] or (coords[0] - 1, coords[1]) in regions[i][3]:
                        if (coords[0] - 1, coords[1]) not in regions[i][3]:
                            r2.append((coords[0] - 1, coords[1]))
                            regions[i][0] += 4
                            regions[i][1] += 1
                            regions[i][3].append((coords[0] - 1, coords[1]))
                        regions[i][0] -= 1
                    else:
                        if not (((coords[0] - 1, coords[1] - 1) not in crops[c] and (coords[0] - 1, coords[1] - 1) not in regions[i][3]) and ((coords[0], coords[1] - 1) in crops[c] or (coords[0], coords[1] - 1) in regions[i][3])):
                            regions[i][2] += 1
                            pass
                    if (coords[0] + 1, coords[1]) in crops[c] or (coords[0] + 1, coords[1]) in regions[i][3]:
                        if (coords[0] + 1, coords[1]) not in regions[i][3]:
                            r2.append((coords[0] + 1, coords[1]))
                            regions[i][0] += 4
                            regions[i][1] += 1
                            regions[i][3].append((coords[0] + 1, coords[1]))
                        regions[i][0] -= 1
                    else:
                        if not (((coords[0] + 1, coords[1] + 1) not in crops[c] and (coords[0] + 1, coords[1] + 1) not in regions[i][3]) and ((coords[0], coords[1] + 1) in crops[c] or (coords[0], coords[1] + 1) in regions[i][3])):
                            regions[i][2] += 1
                    if (coords[0], coords[1] - 1) in crops[c] or (coords[0], coords[1] - 1) in regions[i][3]:
                        if (coords[0], coords[1] - 1) not in regions[i][3]:
                            r2.append((coords[0], coords[1] - 1))
                            regions[i][0] += 4
                            regions[i][1] += 1
                            regions[i][3].append((coords[0], coords[1] - 1))
                        regions[i][0] -= 1
                    else:
                        if not (((coords[0] + 1, coords[1] - 1) not in crops[c] and (coords[0] + 1, coords[1] - 1) not in regions[i][3]) and ((coords[0] + 1, coords[1]) in crops[c] or (coords[0] + 1, coords[1]) in regions[i][3])):
                            regions[i][2] += 1
                    if (coords[0], coords[1] + 1) in crops[c] or (coords[0], coords[1] + 1) in regions[i][3]:
                        if (coords[0], coords[1] + 1) not in regions[i][3]:
                            r2.append((coords[0], coords[1] + 1))
                            regions[i][0] += 4
                            regions[i][1] += 1
                            regions[i][3].append((coords[0], coords[1] + 1))
                        regions[i][0] -= 1
                    else:
                        if not (((coords[0] - 1, coords[1] + 1) not in crops[c] and (coords[0] - 1, coords[1] + 1) not in regions[i][3]) and ((coords[0] - 1, coords[1]) in crops[c] or (coords[0] - 1, coords[1]) in regions[i][3])):
                            regions[i][2] += 1
                for r in r2:
                    crops[c].remove(r)
            price += regions[i][1] * regions[i][2]
            i += 1

print(price)