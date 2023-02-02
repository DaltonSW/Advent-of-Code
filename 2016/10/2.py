import time
import aocd
import os
import re


class Bot:
    def __init__(self, index: int):
        self.index = index
        self.chipOne = None
        self.chipTwo = None
        self.lowPlace = ''
        self.lowIndex = -1
        self.highPlace = ''
        self.highIndex = -1

    def giveChip(self, chip: int):
        if self.chipOne is None:
            self.chipOne = chip
        elif self.chipTwo is None:
            self.chipTwo = chip

    def clearChips(self):
        self.chipOne = None
        self.chipTwo = None

    def setLow(self, s: str):
        s = s.split(' ')
        self.lowPlace = s[0]
        self.lowIndex = int(s[1])

    def setHigh(self, s: str):
        s = s.split(' ')
        self.highPlace = s[0]
        self.highIndex = int(s[1])

    def numChips(self) -> int:
        total = 0
        total += 1 if self.chipOne is not None else 0
        total += 1 if self.chipTwo is not None else 0
        return total


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    data = data.split('\n')
    print(data)

    bots = []
    outputs = []
    for i in range(250):
        bots.append(Bot(i))
        outputs.append([])

    for instruction in data:
        splits = re.findall(r'\w+ \d+', instruction)

        if len(splits) == 2:
            targetBot = bots[int(splits[1].split(' ')[1])]
            targetBot.giveChip(int(splits[0].split(' ')[1]))

        elif len(splits) == 3:
            targetBot = bots[int(splits[0].split(' ')[1])]
            targetBot.setLow(splits[1])
            targetBot.setHigh(splits[2])

    while True:
        for bot in bots:
            if bot.numChips() < 2:
                continue

            if bot.chipOne < bot.chipTwo:
                low = bot.chipOne
                high = bot.chipTwo
            else:
                high = bot.chipOne
                low = bot.chipTwo

            lowPlace = bot.lowPlace
            lowIndex = bot.lowIndex
            highPlace = bot.highPlace
            highIndex = bot.highIndex

            if lowPlace == 'bot':
                bots[lowIndex].giveChip(low)
            else:
                outputs[lowIndex].append(low)

            if highPlace == 'bot':
                bots[highIndex].giveChip(high)
            else:
                outputs[highIndex].append(high)

            bot.clearChips()

            if len(outputs[0]) > 0 and len(outputs[1]) > 0 and len(outputs[2]) > 0:
                print(outputs[0][0] * outputs[1][0] * outputs[2][0])
                time.sleep(20)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
