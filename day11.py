# blinking loop
# find number of stones

with open("day11.txt") as f:
    l = f.readline().split()

stones = {}
new_stones = {}
sum = 0

for stone in l:
    stones[int(stone)] = 1

for _ in range(75):
    for s in stones:
        if s == 0:
            if 1 in new_stones:
                new_stones[1] += stones[s]
            else:
                new_stones[1] = stones[s]
        elif len(str(s)) % 2 == 0:
            if int(str(s)[:int(len(str(s)) / 2)]) in new_stones:
                new_stones[int(str(s)[:int(len(str(s)) / 2)])] += stones[s]
            else:
                new_stones[int(str(s)[:int(len(str(s)) / 2)])] = stones[s]
            if int(str(s)[int(len(str(s)) / 2):]) in new_stones:
                new_stones[int(str(s)[int(len(str(s)) / 2):])] += stones[s]
            else:
                new_stones[int(str(s)[int(len(str(s)) / 2):])] = stones[s]
        else:
            if s * 2024 in new_stones:
                new_stones[s * 2024] += stones[s]
            else:
                new_stones[s * 2024] = stones[s]
    stones = new_stones
    new_stones = {}

for s in stones:
    sum += stones[s]

print(sum)