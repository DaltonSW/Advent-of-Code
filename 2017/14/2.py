import copy
import time
from functools import reduce
from operator import xor
from collections import deque
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

    # data = 'flqrgnkx'

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

    del stringRep, binString, hexString, matrixRow, batch, bit, bits, c, currentPosition, i
    del denseHash, lengths, listLength, numbers, roundNumbers, skipSize, temp, data, cwd, _, hashStr

    neighbors = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    groups = [[]]
    currentGroup = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == '.':
                continue

            if not checkTuple((y, x), groups):
                continue

            else:
                curGroup = groups[currentGroup]
                curGroup.append((y, x))
                temp = deque()
                temp.append((y, x))
                while temp:
                    nY, nX = temp.popleft()
                    for n in neighbors:
                        new = (nY + n[0], nX + n[1])
                        if (new[0] < 0) or (new[0] >= len(matrix)) or (new[1] < 0) or (new[1] >= len(matrix[0])):
                            continue
                        if matrix[new[0]][new[1]] == '#' and checkTuple(new, groups):
                            curGroup.append(new)
                            temp.append(new)
                groups[currentGroup] = curGroup

            currentGroup += 1
            groups.append([])

    print(len(groups) - 1)


def checkTuple(coord: (int, int), groups: [[]]) -> bool:
    for group in groups:
        if coord in group:
            return False
    return True


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

# Submitted answers:
# 3319
# 2087
