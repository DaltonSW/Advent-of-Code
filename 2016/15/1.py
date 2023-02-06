import re
import time
import aocd
import os


class Disc:
    def __init__(self, num: int, positions: int, starting: int):
        self.num = num
        self.numPos = positions
        self.curPos = starting
        self.startPos = starting

    def reset(self):
        self.curPos = self.startPos

    def incPos(self, curTime: int) -> int:
        self.curPos += self.num + curTime
        self.curPos %= self.numPos

        return self.curPos

    def getCurPos(self) -> int:
        return self.curPos


def main():
    discs = []

    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    data = data.split('\n')
    print(data)

    testData = [
        'Disc #1 has 5 positions; at time=0, it is at position 4.',
        'Disc #2 has 2 positions; at time=0, it is at position 1.'
    ]

    data.append('Disc #7 has 11 positions; at time=0, it is at position 0.')

    for d in data:
        nums = re.findall(r'\d+', d)
        discs.append(Disc(int(nums[0]), int(nums[1]), int(nums[3])))

    print()

    t = 0
    while True:
        validTime = True
        for disc in discs:
            disc.reset()
            if disc.incPos(t) != 0:
                validTime = False

        if validTime:
            print(t)
            return
        else:
            t += 1


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
