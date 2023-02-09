import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    data = data.split('\n')
    print(data)

    registers = {
        'a': 12,
        'b': 0,
        'c': 0,
        'd': 0,
    }
    instructions = []

    testData = [
        'cpy 2 a',
        'tgl a',
        'tgl a',
        'tgl a',
        'cpy 1 a',
        'dec a',
        'dec a',
    ]

    for d in data:
        instructions.append(d)

    i = 0
    while i < len(instructions):
        # print(f"{i} - {instructions[i]} -- a: {registers['a']} - b: {registers['b']} - c: {registers['c']} - d: {registers['d']}")
        ins = instructions[i]
        split = ins.split(' ')
        match split[0]:
            case 'xxx':
                i += 1

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
                try:
                    offset = int(split[2])
                except ValueError:
                    offset = registers[split[2]]
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

            case 'tgl':
                target = split[1]
                offset = registers[target]
                try:
                    tempInst = instructions[i + offset]
                    tempSplit = tempInst.split(' ')
                    match tempSplit[0]:
                        case 'cpy':
                            tempSplit[0] = 'jnz'

                        case 'inc':
                            tempSplit[0] = 'dec'

                        case 'dec':
                            tempSplit[0] = 'inc'

                        case 'jnz':
                            tempSplit[0] = 'cpy'

                        case 'tgl':
                            tempSplit[0] = 'inc'

                except IndexError:
                    i += 1
                    continue

                instructions[i + offset] = ' '.join(tempSplit)
                i += 1

    print(registers['a'])


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
