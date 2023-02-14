import time
import aocd
import os
from collections import deque

alphabet = 'abcdefghijklmnopqrstuvwxyz'
queueZero = deque()
queueOne = deque()

def main():
    global alphabet
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))

    instructions = data.split('\n')

    regZero = {x: 0 for x in alphabet}
    regOne = {x: 0 for x in alphabet}
    regOne['p'] = 1

    idxZero = 0
    idxOne = 0

    waitZero = False
    waitTargZero = ''
    waitOne = False
    waitTargOne = ''

    numSent = 0

    while True:
        if not (-1 < idxZero < len(instructions)) or not (-1 < idxOne < len(instructions)):
            break

        if waitZero and waitOne:
            break

        if waitZero and len(queueZero) > 0:
            regZero[waitTargZero] = queueZero.popleft()
            waitZero = False
            waitTargZero = ''
            idxZero += 1

        else:
            instructionZero = instructions[idxZero]
            split = instructionZero.split(' ')
            match split[0]:
                case 'snd':
                    if split[1] in alphabet:
                        queueOne.append(regZero[split[1]])
                    else:
                        queueOne.append(int(split[1]))
                    idxZero += 1

                case 'set':
                    target = split[1]
                    value = split[2]
                    if split[2] in alphabet:
                        regZero[target] = regZero[value]
                    else:
                        regZero[target] = int(value)
                    idxZero += 1

                case 'add':
                    target = split[1]
                    value = split[2]
                    if split[2] in alphabet:
                        regZero[target] += regZero[value]
                    else:
                        regZero[target] += int(value)
                    idxZero += 1

                case 'mul':
                    target = split[1]
                    value = split[2]
                    if split[2] in alphabet:
                        regZero[target] *= regZero[value]
                    else:
                        regZero[target] *= int(value)
                    idxZero += 1

                case 'mod':
                    target = split[1]
                    value = split[2]
                    if split[2] in alphabet:
                        regZero[target] %= regZero[value]
                    else:
                        regZero[target] %= int(value)
                    idxZero += 1

                case 'rcv':
                    target = split[1]
                    if len(queueZero) > 0:
                        regZero[target] = queueZero.popleft()
                        idxZero += 1

                    else:
                        waitZero = True
                        waitTargZero = target

                case 'jgz':
                    target = split[1]
                    offset = split[2]

                    if target in alphabet:
                        target = regZero[target]
                    else:
                        target = int(target)

                    if offset in alphabet:
                        offset = regZero[offset]
                    else:
                        offset = int(offset)

                    if target > 0:
                        idxZero += offset
                    else:
                        idxZero += 1

        if waitOne and len(queueOne) > 0:
            regOne[waitTargOne] = queueOne.popleft()
            waitOne = False
            waitTargOne = ''
            idxOne += 1

        else:
            instructionOne = instructions[idxOne]
            split = instructionOne.split(' ')
            match split[0]:
                case 'snd':
                    if split[1] in alphabet:
                        queueZero.append(regOne[split[1]])
                    else:
                        queueZero.append(int(split[1]))
                    idxOne += 1
                    numSent += 1
                case 'set':
                    target = split[1]
                    value = split[2]
                    if split[2] in alphabet:
                        regOne[target] = regOne[value]
                    else:
                        regOne[target] = int(value)
                    idxOne += 1

                case 'add':
                    target = split[1]
                    value = split[2]
                    if split[2] in alphabet:
                        regOne[target] += regOne[value]
                    else:
                        regOne[target] += int(value)
                    idxOne += 1
                case 'mul':
                    target = split[1]
                    value = split[2]
                    if split[2] in alphabet:
                        regOne[target] *= regOne[value]
                    else:
                        regOne[target] *= int(value)
                    idxOne += 1
                case 'mod':
                    target = split[1]
                    value = split[2]
                    if split[2] in alphabet:
                        regOne[target] %= regOne[value]
                    else:
                        regOne[target] %= int(value)
                    idxOne += 1
                case 'rcv':
                    target = split[1]
                    if len(queueOne) > 0:
                        regOne[target] = queueOne.popleft()
                        idxOne += 1
                    else:
                        waitOne = True
                        waitTargOne = target
                case 'jgz':
                    target = split[1]
                    offset = split[2]
                    if target in alphabet:
                        target = regOne[target]
                    else:
                        target = int(target)
                    if offset in alphabet:
                        offset = regOne[offset]
                    else:
                        offset = int(offset)
                    if target > 0:
                        idxOne += offset
                    else:
                        idxOne += 1

    print(numSent)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
