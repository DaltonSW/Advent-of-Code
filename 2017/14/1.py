import copy
import time
from functools import reduce
from operator import xor

import aocd
import os
from numpy import roll


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    listLength = 256
    numbers = []

    for i in range(listLength):
        numbers.append(i)

    matrix = []

    for i in range(128):
        lengths = []

        hashStr = f'{data}-{i}'

        for c in hashStr:
            lengths.append(ord(c))

        lengths += [17, 31, 73, 47, 23]

        currentPosition = 0
        skipSize = 0
        roundNumbers = copy.deepcopy(numbers)

        for _ in range(64):
            roundNumbers, currentPosition, skipSize = hashNumbers(roundNumbers, lengths, currentPosition, skipSize, listLength)

        roundNumbers.reverse()
        denseHash = []
        for _ in range(16):
            batch = []
            for _ in range(16):
                batch.append(roundNumbers.pop())
            denseHash.append(reduce(xor, batch))

        stringRep = []
        for bits in denseHash:
            temp = hex(bits).split('x')[-1]
            if len(temp) == 1:
                temp = '0' + temp
            stringRep.append(temp)

        hexString = ''.join(stringRep)
        binString = ''
        for c in hexString:
            binString += bin(int(c, 16))[2:].zfill(4)

        matrixRow = []
        for bit in binString:
            matrixRow.append('#' if bit == '1' else '.')
        matrix.append(copy.deepcopy(matrixRow))

    total = 0
    for row in matrix:
        for c in row:
            if c == '#':
                total += 1

    print(total)


def hashNumbers(numbers, lengths, currentPosition, skipSize, listLength) -> ([int], int, int):
    for l in lengths:
        l = int(l)

        numbers = list(roll(numbers, -1 * currentPosition))
        tempArr = numbers[:l]
        numbers = tempArr[::-1] + numbers[l:]
        numbers = list(roll(numbers, currentPosition))

        currentPosition += (skipSize + l) % listLength
        skipSize += 1

    return numbers, currentPosition % listLength, skipSize


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
