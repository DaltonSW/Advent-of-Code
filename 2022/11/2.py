import math
import time


class Monkey:
    isAdd: bool
    opNum: int
    testNum: int
    trueIdx: int
    falseIdx: int
    numInspected: int

    def __init__(self):
        self.items = []
        self.numInspected = 0

    def addItem(self, newItem: int):
        self.items.append(newItem)


def main():
    f = open('input.txt', 'r')

    monkeys = []
    for i in range(8):
        f.readline()  # Throw away monkey index
        monkey = Monkey()
        line = f.readline()
        items = line.split(":")[1].split(",")
        for item in items:
            monkey.addItem(int(item))
        line = f.readline().split(" ")
        try:
            monkey.opNum = int(line[-1])
        except ValueError:
            monkey.opNum = -1
        monkey.isAdd = True if line[-2] == '+' else False
        line = f.readline().split(" ")
        monkey.testNum = int(line[-1])
        line = f.readline().split(" ")
        monkey.trueIdx = int(line[-1])
        line = f.readline().split(" ")
        monkey.falseIdx = int(line[-1])
        monkeys.append(monkey)
        f.readline()  # Throw away empty line

    f.close()

    # remaining code here

    bigMod = 1
    for monkey in monkeys:
        bigMod *= monkey.testNum

    for i in range(10000):
        # print(f"Round {i + 1}")
        for m in range(len(monkeys)):
            monkey = monkeys[m]
            # print(f"\tMonkey {m}")
            if len(monkey.items) == 0:
                continue
            monkey.items.reverse()
            while len(monkey.items) > 0:
                item = monkey.items.pop()
                monkey.numInspected += 1
                # print(f"\t\tMonkey inspects item of worry level {item}")
                opNum = item if monkey.opNum == -1 else monkey.opNum
                if monkey.isAdd:
                    item += opNum
                    # print(f"\t\t\tWorry level increases by {opNum} to {item}")
                else:
                    item *= opNum
                    # print(f"\t\t\tWorry level is multiplied by {opNum} to {item}")
                if item % monkey.testNum == 0:
                    monkeys[monkey.trueIdx].addItem(item % bigMod)
                    # print(f"\t\t\tCurrent worry level is divisible by {monkey.testNum}")
                    # print(f"\t\t\tItem with worry level {item} is thrown to monkey {monkey.trueIdx}")
                else:
                    monkeys[monkey.falseIdx].addItem(item % bigMod)
                    # print(f"\t\t\tCurrent worry level is not divisible by {monkey.testNum}")
                    # print(f"\t\t\tItem with worry level {item} is thrown to monkey {monkey.falseIdx}")

    inspections = []
    for m in range(len(monkeys)):
        print(f"Monkey {m} inspected items {monkeys[m].numInspected} times")
        inspections.append(monkeys[m].numInspected)
    inspections.sort()
    print(inspections[-1] * inspections[-2])


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
