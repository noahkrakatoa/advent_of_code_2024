# make a function to determine if the updates are good
# get all good updates
# add middle numbers

with open("day5.txt") as f:
    lines = f.readlines()

rules = []
updates = []
sum = 0

for l in lines:
    if '|' in l:
        rules.append(l[:-1])
    else:
        updates.append(l[:-1].split(','))

def is_bad(r, u):
    for i in range(len(u)):
        for n in u[i + 1:]:
            if n + '|' + u[i] in r:
                return True
    return False

def fix(r, u):
    for i in range(len(u)):
        for n in u[i + 1:]:
            if n + '|' + u[i] in r:
                u.insert(u.index(n) + 1, u[i])
                u.pop(i)
    if is_bad(r, u):
        return fix(r, u)
    else:
        return int(u[int((len(u) - 1) / 2)])

for u in updates:
    if is_bad(rules, u):
        sum += fix(rules, u)

print(sum)