import time

testData = False
debug = True


def main():
    with open('justLoop.txt', 'r') as inputFile:
        data = inputFile.read()


    data = """S-------7
|F-----7|
||.....||
||.....||
|L-7.F-J|
|..|.|..|
L--J.L--J"""

    print(data)

    rows: list[str] = data.split('\n')
    maze = [[c for c in row] for row in rows]

    totalEnclosed = 0
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            curPos = (row, col)
            if getSpotChar(maze, curPos) != '.':
                continue
            if checkSpot(maze, curPos):
                totalEnclosed += 1

    print(totalEnclosed)

def checkSpot(maze: list[list[str]], curPos: (int, int)) -> bool:
    loopChars = '|-SFJL7'
    row, col = curPos
    invalidCheck = True
    for cRow in range(row - 1, 0, -1):
        spotChar = getSpotChar(maze, (cRow, col))
        if spotChar in loopChars:
            invalidCheck = False
            break
    
    if invalidCheck:
        return False
    invalidCheck = True

    for cRow in range(row + 1, len(maze)):
        spotChar = getSpotChar(maze, (cRow, col))
        if spotChar in loopChars:
            invalidCheck = False
            break

    if invalidCheck:
        return False
    invalidCheck = True

    for cCol in range(col - 1, 0, -1):
        spotChar = getSpotChar(maze, (row, cCol))
        if spotChar in loopChars:
            invalidCheck = False
            break

    if invalidCheck:
        return False
    invalidCheck = True

    for cCol in range(col + 1, len(maze[0])):
        spotChar = getSpotChar(maze, (row, cCol))
        if spotChar in loopChars:
            invalidCheck = False
            break

    if invalidCheck:
        return False

    return True

def getSpotChar(maze: list[list[str]], curPos: (int, int)) -> str:
    return maze[curPos[0]][curPos[1]]


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
