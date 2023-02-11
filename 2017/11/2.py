import copy
import time
import aocd
import os
from collections import deque


class HexNode:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def getTuple(self):
        return self.x, self.y, self.z

    def getDistFromCenter(self):
        return (abs(self.x) + abs(self.y) + abs(self.z)) / 2


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    directions = data.strip().split(',')
    distances = []

    curNode = HexNode(0, 0, 0)

    for direction in directions:
        match direction:
            case 's':
                curNode.y -= 1
                curNode.z += 1
            case 'se':
                curNode.x += 1
                curNode.y -= 1
            case 'ne':
                curNode.x += 1
                curNode.z -= 1
            case 'n':
                curNode.y += 1
                curNode.z -= 1
            case 'nw':
                curNode.x -= 1
                curNode.y += 1
            case 'sw':
                curNode.x -= 1
                curNode.z += 1

        distances.append(curNode.getDistFromCenter())

    goalNode = curNode

    print(goalNode)

    print(max(distances))


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))

