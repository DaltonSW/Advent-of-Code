import time
import aocd
import os
from collections import deque


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))

    spins = int(data)

    lock = deque([0])

    for i in range(1, 50000001):
        lock.rotate(-spins)
        lock.append(i)

    print(lock[lock.index(0) + 1])


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
