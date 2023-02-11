import time
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
    lengths = [3, 4, 1, 5] if testing else data.strip().split(',')

    for l in lengths:
        l = int(l)

        numbers = list(roll(numbers, -1 * currentPosition))
        tempArr = numbers[:l]
        numbers = tempArr[::-1] + numbers[l:]
        numbers = list(roll(numbers, currentPosition))

        currentPosition += (skipSize + l) % listLength
        skipSize += 1
        print(numbers)

    print(numbers[0] * numbers[1])


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
