import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    data = data.split('\n')
    print(data)

    registers = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
    }
    instructions = []

    testData = [
        'cpy 41 a',
        'inc a',
        'inc a',
        'dec a',
        'jnz a 2',
        'dec a',
    ]

    for d in data:
        instructions.append(d)

    i = 0
    while i < len(instructions):
        print(i)
        ins = instructions[i]
        split = ins.split(' ')
        match split[0]:
            case 'cpy':
                target = split[2]
                try:
                    val = int(split[1])
                    registers[target] = val

                except ValueError:
                    registers[target] = registers[split[1]]

                i += 1

            case 'inc':
                target = split[1]
                registers[target] = registers[target] + 1
                i += 1

            case 'dec':
                target = split[1]
                registers[target] = registers[target] - 1
                i += 1

            case 'jnz':
                target = split[1]
                offset = int(split[2])
                try:
                    if registers[target] != 0:
                        i += offset
                    else:
                        i += 1
                except KeyError:
                    if int(target) != 0:
                        i += offset
                    else:
                        i += 1

    print(registers['a'])


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
