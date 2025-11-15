# sort the two columns from least to greatest
# find the difference between the corresponding values from each column
# add them together

column1 = []
column2 = []
sum = 0
sim = 0

with open("day1.txt") as f:
    lines = f.readlines()
    pairs = []
    for l in lines:
        pairs.append(l.split())
    for p in pairs:
        column1.append(int(p[0]))
        column2.append(int(p[1]))

def bubble(c):
    sorted = True
    for i in range(0, len(c) - 1):
        if c[i] > c[i + 1]:
            c[i], c[i + 1] = c[i + 1], c[i]
            sorted = False
    if sorted == False:
        return bubble(c)
    else:
        return c

column1 = bubble(column1)
column2 = bubble(column2)

for i in range(0, len(column1)):
    sum += abs(column1[i] - column2[i])

print(sum)

for n in column1:
    for m in column2:
        if n == m:
            sim += n

print(sim)