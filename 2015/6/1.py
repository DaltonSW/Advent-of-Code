import time
from enum import Enum


class Instruction(Enum):
    ON = 0
    OFF = 1
    TOGGLE = 2


def main():
    f = open('input.txt', 'r')

    lightGrid = [[False] * 1000 for _ in range(1000)]

    for line in f.readlines():
        print(line)
        split = line.strip().split(' ')
        if split[0] == "toggle":
            instruction = Instruction.TOGGLE
            split = split[1:]
        else:
            if split[1] == "off":
                instruction = Instruction.OFF
            else:
                instruction = Instruction.ON
            split = split[2:]
        fromX, fromY = split[0].split(',')
        toX, toY = split[2].split(',')

        for x in range(int(fromX), int(toX) + 1):
            for y in range(int(fromY), int(toY) + 1):
                match instruction:
                    case Instruction.TOGGLE:
                        lightGrid[x][y] = not lightGrid[x][y]
                    case Instruction.ON:
                        lightGrid[x][y] = True
                    case Instruction.OFF:
                        lightGrid[x][y] = False

    f.close()

    # remaining code here

    count = 0
    for row in lightGrid:
        for cell in row:
            if cell:
                count += 1

    print(count)

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
