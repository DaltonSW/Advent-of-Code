import time


def main():
    trees = []
    visible = 0
    f = open('input.txt', 'r')

    for line in f.readlines():
        row = []
        for num in line:
            if num == '\n':
                break
            row.append(int(num))
        trees.append(row)

    f.close()

    # remaining code here
    print(trees)
    visible += (len(trees[0]) - 1) * 4  # Accounting for the edge trees
    for x in range(1, len(trees[0]) - 1):
        for y in range(1, len(trees) - 1):
            if checkTree(x, y, trees):
                visible += 1

    print(visible)


def checkTree(row, col, trees) -> bool:
    height = trees[row][col]
    visible = True
    for x in range(row - 1, -1, -1):
        if not height > trees[x][col]:
            visible = False
            break
    if visible:
        return True

    visible = True
    for x in range(row + 1, len(trees)):
        if not height > trees[x][col]:
            visible = False
            break
    if visible:
        return True

    visible = True
    for y in range(col - 1, -1, -1):
        if not height > trees[row][y]:
            visible = False
            break
    if visible:
        return True

    visible = True
    for y in range(col + 1, len(trees[row])):
        if not height > trees[row][y]:
            visible = False
            break
    if visible:
        return True

    return False

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
