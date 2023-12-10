import time
import aocd
import os

testData = False
debug = True


def main():
    with open('Regexing.txt', 'r') as inputFile:
        data = inputFile.read()

    print(data)

    rows: list[str] = data.split('\n')
    maze = []

    sIndex = (0, 0)

    for rowCount, row in enumerate(rows):
        rowStr: list[str] = [c for c in row]
        maze.append(rowStr)
        if 'S' not in row:
            continue
        sIndex = (rowCount, row.find('S'))
        print(sIndex)

    loopSpots = [sIndex]

    # my input starts with valid moves being north and south
    curDir, curPos = getNextDir(maze, sIndex, 'south')
    del rows, rowCount, row, rowStr, sIndex, data
    while getSpotChar(maze, curPos) != 'S':
        loopSpots.append(curPos)
        curDir, nextPos = getNextDir(maze, curPos, curDir)
        curPos = nextPos

    print(len(loopSpots) // 2)

    with open('newOutput.txt', 'w') as outputFile:
        for i in range(len(maze)):
            outputRow = maze[i]
            for j in range(len(outputRow)):
                if (i, j) not in loopSpots:
                    outputRow[j] = '.'
            outputFile.write(''.join(outputRow))
            outputFile.write('\n')


def getSpotChar(maze: list[list[str]], curPos: (int, int)) -> str:
    return maze[curPos[0]][curPos[1]]

def getNextDir(maze: list[list[str]], curPos: (int, int), curDir: str = None) -> (str, tuple[int, int]):
    dirs = {
        'south': (1, 0),
        'west': (0, -1),
        'east': (0, 1),
        'north': (-1, 0),
    }

    nextSpot = (curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1])
    nextChar = getSpotChar(maze, nextSpot)
    nextDir = ''

    match curDir:
        case 'north':
            match nextChar:
                case '|':
                    nextDir = curDir
                case 'F':
                    nextDir = 'east'
                case '7':
                    nextDir = 'west'

        case 'south':
            match nextChar:
                case '|':
                    nextDir = curDir
                case 'L':
                    nextDir = 'east'
                case 'J':
                    nextDir = 'west'

        case 'east':
            match nextChar:
                case '-':
                    nextDir = curDir
                case 'J':
                    nextDir = 'north'
                case '7':
                    nextDir = 'south'

        case 'west':
            match nextChar:
                case '-':
                    nextDir = curDir
                case 'F':
                    nextDir = 'south'
                case 'L':
                    nextDir = 'north'

    return nextDir, nextSpot

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
