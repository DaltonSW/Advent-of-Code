import copy
import time
import aocd
import os
import re


class Node:
    def __init__(self, x, y, used, avail):
        self.x = x
        self.y = y
        self.used = used
        self.avail = avail

    def __str__(self):
        if self.used > 400:
            return "##/##"
        if self.used == 0:
            return f"__/{self.avail}"
        return f"{self.used}/{self.avail}"


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    nodes = data.split('\n')
    nodes.pop(0)
    nodes.pop(0)

    matrixRow = [None] * 32
    matrix = []
    [matrix.append(copy.deepcopy(matrixRow)) for _ in range(30)]

    for n in nodes:
        split = n.split(' ')
        tempXY = split[0].split('-')
        x, y = int(tempXY[-2][1:]), int(tempXY[-1][1:])
        sizes = re.findall(r'\d+T', n)
        used, avail = int(sizes[1][:-1]), int(sizes[2][:-1])
        matrix[y][x] = Node(x, y, used, avail)

    for row in matrix:
        for n in row:
            print(n, end=' ')
        print()  # This just pretty-prints the input. Solved it by hand. Weird problem


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
