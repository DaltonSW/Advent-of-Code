import time


def main():
    trees = []
    best = -1
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
    # Disregard edge trees, as they'll always be 0
    for x in range(1, len(trees[0]) - 1):
        for y in range(1, len(trees) - 1):
            temp = calcTree(x, y, trees)
            if temp > best:
                best = temp

    print(best)


def calcTree(row, col, trees) -> int:
    height = trees[row][col]
    up, down, left, right = 0, 0, 0, 0
    for x in range(row - 1, -1, -1):
        down += 1
        if height <= trees[x][col]:
            break

    for x in range(row + 1, len(trees)):
        up += 1
        if height <= trees[x][col]:
            break

    for y in range(col - 1, -1, -1):
        left += 1
        if height <= trees[row][y]:
            break

    for y in range(col + 1, len(trees[row])):
        right += 1
        if height <= trees[row][y]:
            break
    score = up * down * left * right
    print("Up: {} - Left: {} - Down: {} - Right: {} -> {}".format(up, left, down, right, score))
    return score



starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
