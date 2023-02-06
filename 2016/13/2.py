import time
import aocd
import os
import sys
import threading
from collections import deque

totalUnderFifty = 0


def main():
    global totalUnderFifty
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

    total = 0
    for y in range(100):
        print(f"Row {y} - {totalUnderFifty}")
        for x in range(100):
            # while threading.active_count() > 20:
            #     pass
            # thread = threading.Thread(target=findShortestPathLength, args=(matrix, (x, y)))
            # thread.start()
            dist = findShortestPathLength(matrix, (1, 1), (x, y))
            if dist <= 50 and dist != -1:
                totalUnderFifty += 1

    print(totalUnderFifty)


# Below 2 functions are implemented from here -- https://www.techiedelight.com/lee-algorithm-shortest-path-in-a-maze/
def isValid(matrix, visited, row, col):
    return (row >= 0) and (row < len(matrix)) and (col >= 0) and (col < len(matrix[0])) \
        and matrix[row][col] == 1 and not visited[row][col]


def findShortestPathLength(mat, src, dest):
    row = [-1, 0, 0, 1]
    col = [0, -1, 1, 0]

    # get source cell (i, j)
    i, j = src

    # get destination cell (x, y)
    x, y = dest

    print(f"(1, 1) -> {dest}")

    # base case: invalid input
    if not mat or len(mat) == 0 or mat[i][j] == 0 or mat[x][y] == 0:
        return -1

    # `M × N` matrix
    (M, N) = (len(mat), len(mat[0]))

    # construct a matrix to keep track of visited cells
    visited = [[False for x in range(N)] for y in range(M)]

    # create an empty queue
    q = deque()

    # mark the source cell as visited and enqueue the source node
    visited[i][j] = True

    # (i, j, dist) represents matrix cell coordinates, and their
    # minimum distance from the source
    q.append((i, j, 0))

    # stores length of the longest path from source to destination
    min_dist = sys.maxsize

    # loop till queue is empty
    while q:

        # dequeue front node and process it
        (i, j, dist) = q.popleft()

        # (i, j) represents a current cell, and `dist` stores its
        # minimum distance from the source

        # if the destination is found, update `min_dist` and stop
        if i == x and j == y:
            min_dist = dist
            break

        # check for all four possible movements from the current cell
        # and enqueue each valid movement
        for k in range(4):
            # check if it is possible to go to position
            # (i + row[k], j + col[k]) from current position
            if isValid(mat, visited, i + row[k], j + col[k]):
                # mark next cell as visited and enqueue it
                visited[i + row[k]][j + col[k]] = True
                q.append((i + row[k], j + col[k], dist + 1))

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
