import time
import aocd
import os
import re


def main():
    cwd = os.getcwd().split('/')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2])).split('\n')
    print(data)

    mappings = {}

    instructions: list[str] = data.pop(0)
    data.pop(0)

    for mapping in data:
        start, left, right = re.findall('\\w{3}', mapping)
        mappings[start] = [left, right]

    currentNode = 'AAA'
    moves = 0
    pendingInstructions = list(instructions)
    pendingInstructions.reverse()

    while currentNode != 'ZZZ':
        if len(pendingInstructions) == 0:
            pendingInstructions = list(instructions)
            pendingInstructions.reverse()
        curInstruction = pendingInstructions.pop()
        output = mappings[currentNode]
        currentNode = output[0] if curInstruction == 'L' else output[1]
        moves += 1

    print(moves)

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
