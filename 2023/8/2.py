import time
import aocd
import os
import re


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2])).split('\n')

    debug = False

    if debug:
        data: list[str] = """LR
        
11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".split('\n')

    # print(data)

    mappings = {}

    instructions: list[str] = data.pop(0)
    data.pop(0)

    currentNodes = []

    for mapping in data:
        start, left, right = re.findall('\\w{3}', mapping)
        mappings[start] = [left, right]
        if start[2] == 'A':
            currentNodes.append(start)

    allMoves = []
    pendingInstructions = list(instructions)
    pendingInstructions.reverse()

    print(currentNodes)

    for i in range(len(currentNodes)):
        currentNode = currentNodes[i]
        moves = 0
        while currentNode[2] != 'Z':
            if len(pendingInstructions) == 0:
                pendingInstructions = list(instructions)
                pendingInstructions.reverse()
            curInstruction = pendingInstructions.pop()
            output = mappings[currentNode]
            currentNode = output[0] if curInstruction == 'L' else output[1]
            moves += 1
        allMoves.append(moves)

    print(allMoves)
    total = 1
    for move in allMoves:
        total *= move
    print(total)

def checkNodes(nodes: list[str]):
    for node in nodes:
        if node[2] != 'Z':
            return False

    return True


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
