import time
import aocd
import os


def main():
    partNumbers: set[int] = set()
    cellsFound: set[str] = set()
    checkedCells: set[(int, int)] = set()
    symbols = "$%=+/#*-&@"
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

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

    specArray = []
    for line in data.split('\n'):
        lineArray = []
        for c in line:
            lineArray.append(c)
        specArray.append(lineArray)

    for rIdx, row in enumerate(specArray):
        for cIdx, cell in enumerate(row):
            cellsFound.add(cell)
            if cell in symbols:
                checkSurrounding(rIdx, cIdx, specArray, partNumbers, checkedCells)

    total = 0
    for num in partNumbers:
        total += num
    print(total)


def checkSurrounding(rIdx, cIdx, specArray, partNumbers, checkedCells):
    for r in range(rIdx - 1, rIdx + 2):
        if r < 0 or r > len(specArray):
            continue
        for c in range(cIdx - 1, cIdx + 2):
            if c < 0 or c > len(specArray[r]):
                continue
            if specArray[r][c].isnumeric():
                partNumbers.add(parseNumber(r, specArray[r], c, checkedCells))


def parseNumber(rowNum: int, row: list[str], startCell: int, checkedCells: set[(int, int)]) -> int:
    number = row[startCell]
    c = startCell
    parseBack, parseForward = True, True
    while parseBack:
        c -= 1
        if (rowNum, c) in checkedCells:
            return 0
        if c < 0:
            parseBack = False
        else:
            cell = row[c]
            if cell.isnumeric():
                checkedCells.add((rowNum, c))
                number = cell + number
            else:
                parseBack = False

    c = startCell
    while parseForward:
        c += 1
        if (rowNum, c) in checkedCells:
            return 0
        if c > len(row) - 1:
            parseForward = False
        else:
            cell = row[c]
            if cell.isnumeric():
                checkedCells.add((rowNum, c))
                number = number + cell
            else:
                parseForward = False

    print("Found: " + number)
    return int(number)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
