import time
import aocd
import os
from copy import deepcopy


class Layer:
    def __init__(self, maximum: int):
        self.maximum = maximum
        self.sensorPos = 0
        self.travelingBack = False

    def setUp(self, num: int):
        self.sensorPos = num % ((self.maximum - 1) * 2)

    def advance(self):
        self.sensorPos += 1
        if self.sensorPos == self.maximum:
            self.sensorPos = (self.maximum - 1) * -1


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    # print(data)

    data = data.split('\n')

    testData = [
        '0: 3',
        '1: 2',
        '4: 4',
        '6: 4',
    ]

    initFirewall = [None] * 90

    for row in data:
        num, maximum = row.split(': ')
        initFirewall[int(num)] = Layer(int(maximum))

    i = 0
    while True:
        firewall = deepcopy(initFirewall)
        i += 1
        # print(i)
        for thing in firewall:
            if isinstance(thing, Layer):
                thing.setUp(i)

        if tryRun(firewall, i):
            print(f"Got it! {i}")
            return


def tryRun(firewall, timeOffset):
    selfPos = 0
    i = 0
    while selfPos < len(firewall):
        i += 1
        curLayer = firewall[selfPos]
        if isinstance(curLayer, Layer) and curLayer.sensorPos == 0:
            return False

        for thing in firewall:
            if isinstance(thing, Layer):
                thing.setUp(timeOffset + i)

        selfPos += 1

    return True


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
