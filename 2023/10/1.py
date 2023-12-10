import time
import aocd
import os

testData = False
debug = True


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))

    if testData:
        data = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

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

    # my input starts with valid moves being north and south
    curDir, curPos = getNextDir(maze, sIndex, 'south')
    del rows, rowCount, row, rowStr, sIndex, data, cwd
    moves = 1
    while getSpotChar(maze, curPos) != 'S':
        curDir, nextPos = getNextDir(maze, curPos, curDir)
        curPos = nextPos
        moves += 1

    print(moves // 2)


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
