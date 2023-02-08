import time
import aocd
import os
from collections import deque
import itertools


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    instructions = data.split('\n')

    string = ['f', 'b', 'g', 'd', 'c', 'e', 'a', 'h']
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    for password in itertools.permutations(characters):
        if scramblePassword(list(password), instructions) == string:
            print(password)
            return


def scramblePassword(string: [str], instructions: list[str]) -> list[str]:
    for inst in instructions:
        split = inst.split(' ')
        match split[0]:
            case 'swap':
                match split[1]:
                    case 'position':
                        x, y = int(split[2]), int(split[5])
                        string[x], string[y] = string[y], string[x]
                    case 'letter':
                        xC, yC = split[2], split[5]
                        x = string.index(xC)
                        y = string.index(yC)
                        string[x], string[y] = string[y], string[x]

            case 'rotate':
                string = deque(string)
                match split[1]:
                    case 'left':
                        string.rotate(int(split[2]) * -1)
                    case 'right':
                        string.rotate(int(split[2]))
                    case 'based':
                        index = string.index(split[-1])
                        string.rotate(1)
                        string.rotate(index)
                        if index >= 4:
                            string.rotate(1)
                string = list(string)

            case 'reverse':
                x, y = int(split[2]), int(split[4]) + 1
                string[x:y] = string[x:y][::-1]

            case 'move':
                x, y = int(split[2]), int(split[5])
                c = string[x]
                del string[x]
                string.insert(y, c)

    return string


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))

# Submitted Answers
# bfaghdce
