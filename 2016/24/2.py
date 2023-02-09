import copy
import time
import aocd
import os
import sys
from collections import deque

successes = []
numLocations = {}


def main():
    global successes, numLocations
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    mazeRows = data.split('\n')
    # print(data)

    matrix = []

    testMazeRows = [
        '###########',
        '#0.1.....2#',
        '#.#######.#',
        '#4.......3#',
        '###########',
    ]

    for row in mazeRows:
        matrixRow = []
        for c in row:
            matrixRow.append(c)
        matrix.append(matrixRow)

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            val = matrix[y][x]
            if val != '#' and val != '.':
                numLocations[val] = (y, x)

    for row in matrix:
        for i in range(len(row)):
            c = row[i]
            if c == '#':
                c = 0
            else:
                c = 1
            row[i] = c

    start = numLocations['0']

    traverseMaze(start, matrix, 0, list(numLocations.values()))
    newVals = []
    for pair in successes:
        newVals.append(pair[0] + findShortestPathLength(matrix, pair[1], start))

    print(min(newVals))


def traverseMaze(pos: (int, int), matrix: [[str]], curJourney: int, positionsLeft: []):
    global successes, numLocations
    if pos in positionsLeft:
        positionsLeft.remove(pos)
        if len(positionsLeft) == 0:
            successes.append((curJourney, pos))
            return

    for newPos in positionsLeft:
        lenToNum = findShortestPathLength(matrix, pos, newPos)
        if lenToNum != -1:
            newList = copy.deepcopy(positionsLeft)
            traverseMaze(newPos, matrix, curJourney + lenToNum, newList)


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

    # print(f"(1, 1) -> {dest}")

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


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
