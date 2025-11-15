# locate every mul()
# multiply them
# add them

line = ''

with open("day3.txt") as f:
    lines = f.readlines()
    for l in lines:
        line += l

sum = 0

def is_mul(l, i):
    if l[i:i + 4] == 'mul(':
        num1 = ''
        num2 = ''
        n = 0
        while True:
            if 48 <= ord(l[i + 4 + n]) <= 57:
                num1 += l[i + 4 + n]
                n += 1
            elif l[i + 4 + n] == ',':
                break
            else:
                return False
        m = 1
        while True:
            if 48 <= ord(l[i + 4 + n + m]) <= 57:
                num2 += l[i + 4 + n + m]
                n += 1
            elif l[i + 4 + n + m] == ')':
                break
            else:
                return False
        if 1 <= len(num1) <= 3 and 1 <= len(num2) <= 3:
            return int(num1) * int(num2)
        else:
            return False
    else:
        return False

do = True
for l in lines:
    for i in range(len(l) - 7):
        if l[i:i + 4] == 'do()':
            do = True
            print('do')
        elif l[i:i + 7] == 'don\'t()':
            do = False
            print('don\'t')
        if is_mul(l, i) and do:
            sum += is_mul(l, i)

print(sum)