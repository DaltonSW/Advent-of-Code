import time
import aocd
import os
import sys


def main():

    matrix = []
    for _ in range(100):
        matrixRow = [0] * 100
        matrix.append(matrixRow)

    cwd = os.getcwd().split('\\')
    data = int(aocd.get_data(None, int(cwd[-1]), int(cwd[-2])))
    print(data)

    for y in range(100):
        for x in range(100):
            val = 1 if isOpenSpace(x, y, data) else 0
            matrix[y][x] = val
            print(val, end='')
        print()

    print(findShortestPathLength(matrix))


def isSafe(matrix, visited, x, y):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and \
        not (matrix[x][y] == 0 or visited[x][y])


# Find the shortest possible route in a matrix `mat` from source cell (i, j)
# to destination cell `dest`.

# `min_dist` stores the length of the longest path from source to a destination
# found so far, and `dist` maintains the length of the path from a source cell to
# the current cell (i, j).

def findShortestPath(matrix, visited, i, j, dest, min_dist=sys.maxsize, dist=0):
    # if the destination is found, update `min_dist`
    if (i, j) == dest:
        return min(dist, min_dist)

    # set (i, j) cell as visited
    visited[i][j] = 1

    # go to the bottom cell
    if isSafe(matrix, visited, i + 1, j):
        min_dist = findShortestPath(matrix, visited, i + 1, j, dest, min_dist, dist + 1)

    # go to the right cell
    if isSafe(matrix, visited, i, j + 1):
        min_dist = findShortestPath(matrix, visited, i, j + 1, dest, min_dist, dist + 1)

    # go to the top cell
    if isSafe(matrix, visited, i - 1, j):
        min_dist = findShortestPath(matrix, visited, i - 1, j, dest, min_dist, dist + 1)

    # go to the left cell
    if isSafe(matrix, visited, i, j - 1):
        min_dist = findShortestPath(matrix, visited, i, j - 1, dest, min_dist, dist + 1)

    # backtrack: remove (i, j) from the visited matrix
    visited[i][j] = 0

    return min_dist


# Wrapper over findShortestPath() function
def findShortestPathLength(matrix):
    # get source cell (i, j)
    i, j = 1, 1

    # get destination cell (x, y)
    x, y = 39, 31

    # base case
    if not matrix or len(matrix) == 0 or matrix[i][j] == 0 or matrix[x][y] == 0:
        return -1

    # `M × N` matrix
    (M, N) = (len(matrix), len(matrix[0]))

    # construct an `M × N` matrix to keep track of visited cells
    visited = [[False for _ in range(N)] for _ in range(M)]

    min_dist = findShortestPath(matrix, visited, i, j, (x, y))

    if min_dist != sys.maxsize:
        return min_dist
    else:
        return -1


def isOpenSpace(x: int, y: int, favNum: int) -> bool:
    val = (x * x) + (3 * x) + (2 * x * y) + y + (y * y)
    val += favNum
    total = 0
    binary = bin(val)
    # print(binary)
    for c in binary[2:]:
        if c == '1':
            total += 1

    return True if total % 2 == 0 else False


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
