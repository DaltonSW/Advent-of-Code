import time
import aocd
import os

dirs = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

grid = {
    (-2, 0): "1",
    (-1, -1): "2",
    (-1, 0): "3",
    (1, -1): "4",
    (0, -2): "5",
    (0, -1): "6",
    (0, 0): "7",
    (0, 1): "8",
    (0, 2): "9",
    (1, -1): "A",
    (1, 0): "B",
    (1, 1): "C",
    (2, 0): "D",
}


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))

    # f = open('input.txt', 'r')
    # data = ""
    # for line in f.readlines():
    #     data += line
    # f.close()

    curPos = (0, -2)
    for c in data:
        if c == '\n':
            print(grid[curPos])
            continue
        else:
            change = dirs[c]
            newZero = curPos[0] + change[0]
            newOne = curPos[1] + change[1]
            try:
                newPos = (newZero, newOne)
                val = grid[newPos]
                curPos = newPos
            except KeyError:
                continue

    print(grid[curPos])


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
