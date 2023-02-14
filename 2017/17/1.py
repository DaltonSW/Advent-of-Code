import time
import aocd
import os
from numpy import roll


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    # print(data)

    spins = int(data)
    # spins = 3

    lock = [0]
    for i in range(1, 2018):
        if len(lock) < spins:
            lock = list(roll(lock, spins))
        else:
            lock = lock[-1 * spins:] + lock[:-1 * spins]
        lock.insert(1, i)

    print(lock[lock.index(2017) - 1])


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
