import re
import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    # print(data)

    # testData = '.^^.^.^^^^'

    entireGrid = [data]

    for r in range(39):
        row = entireGrid[r]
        newRow = isTrap(False, row[0] == '^', row[1] == '^')
        for i in range(1, len(row) - 1):
            newRow += isTrap(row[i - 1] == '^', row[i] == '^', row[i + 1] == '^')
        newRow += isTrap(row[-2] == '^', row[-1] == '^', False)
        entireGrid.append(newRow)

    totalSafe = 0
    for row in entireGrid:
        totalSafe += len(re.findall(r'\.', row))
        print(row)

    print(totalSafe)


def isTrap(left: bool, center: bool, right: bool) -> str:
    if left and center and not right:
        return '^'
    if not left and center and right:
        return '^'
    if left and not center and not right:
        return '^'
    if not left and not center and right:
        return '^'
    return '.'



starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
