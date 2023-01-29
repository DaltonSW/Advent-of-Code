import time


def main():
    f = open('input.txt', 'r')

    lightGrid = []

    for line in f.readlines():
        row = []
        line = line.strip()
        for c in line:
            val = True if c == '#' else False
            row.append(val)
        lightGrid.append(row)
        print(line)
        # parsing code here

    f.close()

    # remaining code here

    print()
    for i in range(100):
        changeGrid = [[False] * 1000 for _ in range(1000)]
        for y in range(len(lightGrid)):
            row = lightGrid[y]
            for x in range(len(row)):
                n = getNeighbors(lightGrid, x, y)
                if lightGrid[x][y]:
                    changeGrid[x][y] = True if len(n) == 2 or len(n) == 3 else False
                else:
                    changeGrid[x][y] = True if len(n) == 3 else False

        changeGrid[0][0] = True
        changeGrid[0][99] = True
        changeGrid[99][0] = True
        changeGrid[99][99] = True

        for y in range(len(lightGrid)):
            row = lightGrid[y]
            for x in range(len(row)):
                lightGrid[x][y] = changeGrid[x][y]

        for row in lightGrid:
            output = ""
            for item in row:
                output += '#' if item else '.'
            print(output)
        print()

    count = 0
    for row in lightGrid:
        for item in row:
            if item:
                count += 1

    print(count)


def getNeighbors(matrix, x, y):
    num_rows, num_cols = len(matrix), len(matrix[0])
    result = []

    for i in range((0 if x - 1 < 0 else x - 1), (num_rows if x + 2 > num_rows else x + 2), 1):
        for j in range((0 if y - 1 < 0 else y - 1), (num_cols if y + 2 > num_cols else y + 2), 1):
            if (i, j) != (x, y) and matrix[i][j]:
                result.append(matrix[i][j])
    return result


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
