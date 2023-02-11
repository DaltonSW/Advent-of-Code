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


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    directions = data.strip().split(',')

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

    goalNode = curNode

    print(goalNode)

    space = deque()
    start = HexNode(0, 0, 0)
    space.append(start)

    cameFrom = {start.getTuple(): None}

    while len(space) > 0:
        curSpace = space.popleft()
        if curSpace.getTuple() == goalNode.getTuple():
            break

        neighbors = [
            HexNode(curSpace.x, curSpace.y - 1, curSpace.z + 1),
            HexNode(curSpace.x + 1, curSpace.y - 1, curSpace.z),
            HexNode(curSpace.x + 1, curSpace.y, curSpace.z - 1),
            HexNode(curSpace.x, curSpace.y + 1, curSpace.z - 1),
            HexNode(curSpace.x - 1, curSpace.y + 1, curSpace.z),
            HexNode(curSpace.x - 1, curSpace.y, curSpace.z + 1),
        ]

        for n in neighbors:
            try:
                _ = cameFrom[n.getTuple()]

            except KeyError:
                cameFrom[n.getTuple()] = curSpace
                space.append(n)

    prev = goalNode
    moves = -1
    while prev is not None:
        moves += 1
        prev = cameFrom[prev.getTuple()]

    print(moves)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
