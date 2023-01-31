import time
import aocd
import os

dirs = {
    "U": [-1, 0],
    "D": [1, 0],
    "L": [0, -1],
    "R": [0, 1]
}

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))

    # f = open('test.txt', 'r')
    # data = ""
    # for line in f.readlines():
    #     data += line
    # f.close()

    curPos = [1, 1]
    for c in data:
        if c == '\n':
            print(grid[curPos[0]][curPos[1]])
            continue
        else:
            change = dirs[c]
            newX = curPos[0] + change[0]
            newY = curPos[1] + change[1]
            if newX < 0 or newX > 2 or newY < 0 or newY > 2:
                continue
            else:
                curPos = [newX, newY]
    print(grid[curPos[0]][curPos[1]])


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
