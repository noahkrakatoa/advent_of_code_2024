# look at all possible combinations
# check each
# add test values

with open("day7.txt") as f:
    l = f.readlines()

sum = 0

for i in range(len(l)):
    l[i] = l[i].split(': ')
    l[i][1] = l[i][1].split(' ')
    if i != len(l) - 1:
        l[i][1][-1] = l[i][1][-1][:-1]

for line in l:
    numbers = [line[1][0]]
    for n in line[1][1:]:
        fnumbers = []
        for i in range(len(numbers)):
            fnumbers.append(numbers[i])
        for m in fnumbers:
            numbers.append(int(m) + int(n))
            numbers.append(int(m) * int(n))
            numbers.append(str(m) + str(n))
            numbers.pop(0)
    if int(line[0]) in numbers or line[0] in numbers:
        sum += int(line[0])

print(sum)