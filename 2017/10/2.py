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

    testing = False

    listLength = 5 if testing else 256
    numbers = []

    for i in range(listLength):
        numbers.append(i)

    currentPosition = 0
    skipSize = 0
    lengths = []

    for c in data.strip():
        lengths.append(ord(c))

    lengths += [17, 31, 73, 47, 23]

    for _ in range(64):
        numbers, currentPosition, skipSize = hashNumbers(numbers, lengths, currentPosition, skipSize, listLength)

    numbers.reverse()
    denseHash = []
    for _ in range(16):
        batch = []
        for _ in range(16):
            batch.append(numbers.pop())
        denseHash.append(reduce(xor, batch))

    stringRep = []
    for bits in denseHash:
        temp = hex(bits).split('x')[-1]
        if len(temp) == 1:
            temp = '0' + temp
        stringRep.append(temp)

    print(''.join(stringRep))


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
