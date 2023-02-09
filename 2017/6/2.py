import re
import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)
    numbers = re.findall(r'\d+', data)
    numbers = [int(x) for x in numbers]

    seenStates = {}
    cycles = 0
    dupeCounter = 0
    dupe = None

    while True:
        val = max(numbers)
        i = numbers.index(val)
        numbers[i] = 0
        cycles += 1
        dupeCounter += 1
        while val > 0:
            i = (i + 1) % len(numbers)
            numbers[i] += 1
            val -= 1
        stateTuple = tuple(numbers)
        if stateTuple == dupe:
            print(dupeCounter)
            return
        try:
            seenStates[stateTuple] += 1
            if dupe is None:
                dupe = stateTuple
                dupeCounter = 0
            print(stateTuple)
            print(cycles)
        except KeyError:
            seenStates[stateTuple] = 1


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
