# determine if a single function is safe
# figure out how many are safe

with open("day2.txt") as f:
    reports = f.readlines()

safe_reports = 0

def safety(r):
    mode = None
    for i in range(len(r) - 1):
        fmode = mode
        if int(r[i]) - int(r[i + 1]) > 0:
            mode = 0
        elif int(r[i]) - int(r[i + 1]) < 0:
            mode = 1
        else:
            return False
        if fmode != None and fmode != mode:
                return False
        elif abs(int(r[i]) - int(r[i + 1])) > 3:
            return False
    return True

for r in reports:
    safe = False
    r = r.split()
    for i in range(len(r)):
        if safety(r[:i] + r[i + 1:]):
            safe = True
    if safe or safety(r):
        safe_reports += 1

print(safe_reports)