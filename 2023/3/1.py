import time
import aocd
import os

# Attempted Answers:
# 314790 -- Too low
# 535351 -- Correct!!


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

    partNumbers: list[int] = []
    symbols = "$%=+/#*-&@"

    for rIndex, row in enumerate(spec):
        cIndex = 0
        while cIndex < len(row):
            cell: str = row[cIndex]
            if cell.isnumeric():
                cIndex += checkNumber(rIndex, cIndex, spec, partNumbers, symbols)
            else:
                cIndex += 1

    total = 0
    for num in partNumbers:
        total += num
    print(total)

def checkNumber(rIndex, cIndex, spec, partNumbers, symbols) -> int:
    row = spec[rIndex]
    number = ""
    c = cIndex
    while True:
        cell = row[c]
        if not cell.isnumeric():
            break
        number += cell
        c += 1
        if c >= len(row):
            break

    numLen = len(number)
    if cIndex - 1 >= 0 and row[cIndex - 1] in symbols:
        partNumbers.append(int(number))
        print("Found: " + number)
        return numLen

    if cIndex + numLen < len(row) and row[cIndex + numLen] in symbols:
        partNumbers.append(int(number))
        print("Found: " + number)
        return numLen

    for r in [rIndex - 1, rIndex + 1]:
        if r < 0 or r >= len(spec):
            continue
        for c in range(cIndex - 1, cIndex + numLen + 1):
            if c < 0 or c >= len(row):
                continue
            if spec[r][c] in symbols:
                partNumbers.append(int(number))
                print("Found: " + number)
                return numLen
    return numLen

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
