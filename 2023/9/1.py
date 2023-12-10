import time
import aocd
import os
import re

def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    # print(data)

    debug = False

    if debug:
        data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

    histories = data.split('\n')

    total = 0
    for history in histories:
        total += parseHistories(history)

    print(total)


def parseHistories(history):
    layers = []
    currentLayer = [int(x) for x in history.split()]
    total = 0
    while True:
        layers.append(currentLayer)
        nextLayer = []
        for i in range(len(currentLayer) - 1):
            nextLayer.append(currentLayer[i + 1] - currentLayer[i])

        if len(set(nextLayer)) == 1 and 0 in nextLayer:
            if len(currentLayer) > 0:
                total += currentLayer[-1]
            return total

        else:
            print(currentLayer)
            if len(currentLayer) > 0:
                total += currentLayer[-1]
            currentLayer = nextLayer

if __name__ == '__main__':
    starttime = time.time()
    main()
    endtime = time.time()

    print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
