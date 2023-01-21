import time
from bresenham import bresenham

class Node:
    def __init__(self, dirs: str):
        temp = dirs.split(',')
        self.x, self.y = int(temp[0]), int(temp[1])
        self.nextNode = None

    def setNextNode(self, newNode):
        self.nextNode = newNode


class Instruction:
    def __init__(self):
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)


def main():
    f = open('input.txt', 'r')

    sandSpawnPos = (500, 0)

    matrix = []
    for _ in range(166):
        matrixRow = []
        for _ in range(575):
            matrixRow.append('.')
        matrix.append(matrixRow)

    instructions = []
    for line in f.readlines():
        instruction = Instruction()
        dirsList = line.strip().split(' -> ')
        for dirs in dirsList:
            instruction.addNode(Node(dirs))

        instructions.append(instruction)

    f.close()

    # remaining code here

    for inst in instructions:
        for i in range(len(inst.nodes) - 1):
            line = list(bresenham(inst.nodes[i].x, inst.nodes[i].y, inst.nodes[i + 1].x, inst.nodes[i + 1].y))
            plotPoints(line, matrix)

    matrix[sandSpawnPos[1]][sandSpawnPos[0]] = '+'

    for row in matrix:
        for c in row:
            print(c, end='')
        print()

    count = 0
    while True:
        count += 1
        sandFalling = True
        sandPosX, sandPosY = sandSpawnPos
        while sandFalling:
            try:
                if matrix[sandPosY + 1][sandPosX] == '.':  # Check down one
                    sandPosY += 1

                elif matrix[sandPosY + 1][sandPosX - 1] == '.':  # Check down left
                    sandPosX -= 1
                    sandPosY += 1

                elif matrix[sandPosY + 1][sandPosX + 1] == '.':  # Check down right
                    sandPosX += 1
                    sandPosY += 1

                else:
                    matrix[sandPosY][sandPosX] = 'o'
                    sandFalling = False
                    # for row in matrix:
                    #     for i in range(430, len(row)):
                    #         c = row[i]
                    #         print(c, end='')
                    #     print()
            except IndexError:
                print(count - 1)
                return


def plotPoints(newPoints, matrix):
    for point in newPoints:
        x, y = point[0], point[1]
        matrix[y][x] = '#'


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
