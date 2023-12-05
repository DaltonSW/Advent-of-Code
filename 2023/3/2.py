import time
import aocd
import os

# Attempted Answers:


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))

#     data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""
    print(data)

    spec = []
    for line in data.split('\n'):
        lineArray = []
        for c in line:
            lineArray.append(c)
        spec.append(lineArray)

    total = 0

    for rIndex, row in enumerate(spec):
        cIndex = 0
        while cIndex < len(row):
            cell: str = row[cIndex]
            if cell == "*":
                total += checkCell(rIndex, cIndex, spec)
            cIndex += 1

    print(total)

def checkCell(row, col, spec):
    neighbors = set()
    for i in range(row - 1, row + 2):
        if i < 0 or i > len(spec):
            continue
        for j in range(col - 1, col + 2):
            if j < 0 or j > len(spec[i]):
                continue
            if spec[i][j].isnumeric():
                neighbors.add(parseNumber(spec[i], j))
    if len(neighbors) != 2:
        return 0

    return neighbors.pop() * neighbors.pop()

def parseNumber(row: list[str], startCell: int) -> int:
    number = row[startCell]
    c = startCell
    parseBack, parseForward = True, True
    while parseBack:
        c -= 1
        if c < 0:
            parseBack = False
        else:
            cell = row[c]
            if cell.isnumeric():
                number = cell + number
            else:
                parseBack = False

    c = startCell
    while parseForward:
        c += 1
        if c > len(row) - 1:
            parseForward = False
        else:
            cell = row[c]
            if cell.isnumeric():
                number = number + cell
            else:
                parseForward = False

    print("Found: " + number)
    return int(number)

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
