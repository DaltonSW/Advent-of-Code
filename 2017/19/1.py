import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    dirs = {
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
        'up': (-1, 0),
    }

    alpha = 'ABCDEFGHIJKLMNOPQRS'

    end = 'S'  # It's on the far right, toward the top
    testEnd = 'F'
    # end = testEnd
    curDir = 'down'

    testData = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
"""

    mazeInput = data.split('\n')
    maze = []

    for row in mazeInput:
        maze.append([c for c in row])

    visitedLetters = []
    start = (0, maze[0].index('|'))
    curPos = start
    while True:
        curMove = dirs[curDir]
        curPos = (curPos[0] + curMove[0], curPos[1] + curMove[1])
        curChar = maze[curPos[0]][curPos[1]]
        if curChar in alpha:
            visitedLetters.append(curChar)
            if curChar == end:
                break

        elif maze[curPos[0]][curPos[1]] == '+':
            if curDir == 'up' or curDir == 'down':
                leftChar = maze[curPos[0]][curPos[1] - 1]
                if leftChar == '-' or leftChar in alpha:
                    curDir = 'left'
                else:
                    rightChar = maze[curPos[0]][curPos[1] + 1]
                    if rightChar == '-' or rightChar in alpha:
                        curDir = 'right'

            elif curDir == 'left' or curDir == 'right':
                upChar = maze[curPos[0] - 1][curPos[1]]
                if upChar == '|' or upChar in alpha:
                    curDir = 'up'
                else:
                    downChar = maze[curPos[0] + 1][curPos[1]]
                    if downChar == '|' or downChar in alpha:
                        curDir = 'down'

    print(''.join(visitedLetters))

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
