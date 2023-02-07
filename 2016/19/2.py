import time
import aocd
import os
from collections import deque


class Elf:
    def __init__(self, number: int):
        self.number = number
        self.presents = 1

    def getPresents(self) -> int:
        return self.presents


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    # print(data)

    elves = deque()

    testing = False
    numElves = 5 if testing else int(data)

    [elves.append(Elf(i)) for i in range(numElves)]

    while len(elves) > 1:
        if len(elves) % 1000 == 0:
            print(f"{len(elves)} -- {time.strftime('%I:%M:%S', time.localtime())}")
        elf = elves.popleft()
        if elf.getPresents() != 0:
            targetIndex = (len(elves) - 1) // 2
            target = elves[targetIndex]
            elf.presents += target.getPresents()
            # print(f"Elf {elf.number + 1} takes Elf {target.number + 1}'s {target.getPresents()} presents.")
            elves.remove(target)
            elves.append(elf)

    print(elves[0].number + 1)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
