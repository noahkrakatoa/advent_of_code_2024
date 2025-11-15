# split input
# for loop for each instruction
# get output

with open("day17.txt") as f:
    l = f.readlines()

registers = [0, 0, 0]
program = [2, 4, 1, 1, 7, 5, 4, 7, 1, 4, 0, 3, 5, 5, 3, 0]
output = ''
i = 0
a = 175950000000000

print(registers)
print(program)

while True:
    registers = [0, 0, 0]
    program = [2, 4, 1, 1, 7, 5, 4, 7, 1, 4, 0, 3, 5, 5, 3, 0]
    output = []
    i = 0
    registers[0] = a
    correct = 0
    while i < len(program):
        opcode = int(program[i])
        operand = int(program[i + 1])
        opbits = [int(operand / 4) % 2, int((operand - int(operand / 4) * 4) / 2), int(operand - int(operand / 4) * 4) % 2]

        if operand < 4:
            combo = operand
        elif 3 < operand < 7:
            combo = registers[operand - 4]
    
        if opcode == 0:
            registers[0] = int(registers[0] / 2 ** combo)
        elif opcode == 1:
            registers[1] = registers[1] ^ operand
        elif opcode == 2:
            registers[1] = combo % 8
        elif opcode == 3:
            if registers[0] != 0:
                i = operand - 2
        elif opcode == 4:
            registers[1] = registers[1] ^ registers[2]
        elif opcode == 5:
            output.append(combo % 8)
        elif opcode == 6:
            registers[1] = int(registers[0] / 2 ** combo)
        else:
            registers[2] = int(registers[0] / 2 ** combo)
        i += 2
    if output == program:
        break
    a += 1
    print(output)
    print(len(program) - len(output))
    for j in range(len(program) - 1, -1, -1):
        if output[j] == program[j]:
            correct += 1
    print(correct)

print(a)