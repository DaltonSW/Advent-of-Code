import time
import aocd
import os

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def main():
    global alphabet
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    # print(data)

    testData = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""

    instructions = data.split('\n')
    registers = {x: 0 for x in alphabet}
    sounds = []

    i = 0
    while 0 <= i < len(instructions):
        instruction = instructions[i]
        split = instruction.split(' ')
        match split[0]:
            case 'snd':
                sounds.append(registers[split[1]])
                i += 1

            case 'set':
                target = split[1]
                value = split[2]
                if split[2] in alphabet:
                    registers[target] = registers[value]
                else:
                    registers[target] = int(value)
                i += 1

            case 'add':
                target = split[1]
                value = split[2]
                if split[2] in alphabet:
                    registers[target] += registers[value]
                else:
                    registers[target] += int(value)
                i += 1

            case 'mul':
                target = split[1]
                value = split[2]
                if split[2] in alphabet:
                    registers[target] *= registers[value]
                else:
                    registers[target] *= int(value)
                i += 1

            case 'mod':
                target = split[1]
                value = split[2]
                if split[2] in alphabet:
                    registers[target] %= registers[value]
                else:
                    registers[target] %= int(value)
                i += 1

            case 'rcv':
                target = split[1]
                if registers[target] != 0:
                    sound = sounds.pop()
                    print(sound)
                    return
                else:
                    i += 1

            case 'jgz':
                target = split[1]
                offset = split[2]

                if target in alphabet:
                    target = registers[target]
                else:
                    target = int(target)

                if offset in alphabet:
                    offset = registers[offset]
                else:
                    offset = int(offset)

                if target > 0:
                    i += offset
                else:
                    i += 1


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
