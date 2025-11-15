# check all horizontal and vertical XMAS's
# check all diagonal XMAS's
# find the sum

with open("day4.txt") as f:
    l = f.readlines()

sum = 0
sim = 0

for n in range(len(l)):
    for m in range(len(l[0]) - 1):
        if l[n][m] == 'X':
            if n >= 3:
                if l[n - 1][m] + l[n - 2][m] + l[n - 3][m] == 'MAS':
                    sum += 1
            if n <= len(l) - 4:
                if l[n + 1][m] + l[n + 2][m] + l[n + 3][m] == 'MAS':
                    sum += 1
            if m >= 3:
                if l[n][m - 1] + l[n][m - 2] + l[n][m - 3] == 'MAS':
                    sum += 1
            if m <= len(l[0]) - 4:
                if l[n][m + 1] + l[n][m + 2] + l[n][m + 3] == 'MAS':
                    sum += 1
            
            if n >= 3 and m >= 3:
                if l[n - 1][m - 1] + l[n - 2][m - 2] + l[n - 3][m - 3] == 'MAS':
                    sum += 1
            if n >= 3 and m <= len(l[0]) - 4:
                if l[n - 1][m + 1] + l[n - 2][m + 2] + l[n - 3][m + 3] == 'MAS':
                    sum += 1
            if n <= len(l) - 4 and m >= 3:
                if l[n + 1][m - 1] + l[n + 2][m - 2] + l[n + 3][m - 3] == 'MAS':
                    sum += 1
            if n <= len(l) - 4 and m <= len(l[0]) - 4:
                if l[n + 1][m + 1] + l[n + 2][m + 2] + l[n + 3][m + 3] == 'MAS':
                    sum += 1

print(sum)

for n in range(len(l) - 2):
    for m in range(0, len(l[0]) - 3):
        if (l[n][m] + l[n + 1][m + 1] + l[n + 2][m + 2] == 'MAS' or l[n][m] + l[n + 1][m + 1] + l[n + 2][m + 2] == 'SAM') and (l[n][m + 2] + l[n + 1][m + 1] + l[n + 2][m] == 'MAS' or l[n][m + 2] + l[n + 1][m + 1] + l[n + 2][m] == 'SAM'):
            sim += 1

print(sim)