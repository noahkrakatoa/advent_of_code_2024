# change disk map into file
# free space on file
# calculate checksum

with open("day9.txt") as f:
    disk_map = f.readline()

files = []
checksum = 0
id_number = 0

for i in range(len(disk_map)):
    if i % 2 == 0:
        files.append([str(id_number) for _ in range(int(disk_map[i]))])
        id_number += 1
    else:
        files.append(['.' for _ in range(int(disk_map[i]))])

print(files)
n = len(files) - 1

while True:
    f2 = []
    for file in files:
        f2.append([block for block in file])
    m = 0
    if files[n] != [] and files[n][0].isnumeric():
        while True:
            if m > n:
                break
            elif '.' in files[m]:
                periods = 0
                for c in files[m]:
                    if c == '.':
                        periods += 1
                if len(files[n]) <= periods:
                    b = 0
                    c = 0
                    while True:
                        same = True
                        for block in files[n]:
                            if block.isnumeric():
                                same = False
                        if same == True:
                            break
                        if files[m][b] == '.':
                            files[m][b], files[n][c] = files[n][c], files[m][b]
                            c += 1
                        b += 1
            m += 1
    n -= 1

    if files == f2 and n == 0:
        break

i = 0

print(files)

for file in files:
    for block in file:
        if block.isnumeric():
            checksum += i * int(block)
        i += 1
            
print(checksum)