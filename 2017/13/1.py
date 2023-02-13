import time
import aocd
import os


class Layer:
    def __init__(self, maximum: int):
        self.maximum = maximum
        self.sensorPos = 0
        self.travelingBack = False

    def advance(self):
        if self.travelingBack:
            self.sensorPos -= 1
            if self.sensorPos == 0:
                self.travelingBack = False
        else:
            self.sensorPos += 1
            if self.sensorPos == self.maximum - 1:
                self.travelingBack = True


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

    firewall = [None] * 100

    for row in data:
        num, maximum = row.split(': ')
        firewall[int(num)] = Layer(int(maximum))

    selfPos = 0
    totalSeverity = 0
    while selfPos < len(firewall):
        curLayer = firewall[selfPos]
        if isinstance(curLayer, Layer) and curLayer.sensorPos == 0:
            totalSeverity += selfPos * curLayer.maximum

        for thing in firewall:
            if isinstance(thing, Layer):
                thing.advance()

        selfPos += 1

    print(totalSeverity)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
