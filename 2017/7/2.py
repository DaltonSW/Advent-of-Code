import time
import aocd
import os


class Process:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        self.subProcs = {}
        self.parentProc = None

    def getHoldingWeight(self) -> int:
        total = self.weight
        subProcWeights = {}
        for subProc in self.subProcs.values():
            subWeight = subProc.getHoldingWeight()
            try:
                subProcWeights[subWeight] += 1
            except KeyError:
                subProcWeights[subWeight] = 1
            total += subWeight
        if len(subProcWeights) > 1:
            print("Mismatch found!!!")
            for weight in subProcWeights.keys():
                if subProcWeights[weight] > 1:
                    correctWeight = weight
                    # print(f"Should be {weight}")
                elif subProcWeights[weight] == 1:
                    incorrectWeight = weight
                    # print(f"Wrong weight is {weight}")
            for subProc in self.subProcs.values():
                if subProc.getHoldingWeight() == incorrectWeight:
                    print(f"{subProc.name} should be {subProc.weight - abs(correctWeight - incorrectWeight)}")
        # print(f"{self.name} -- {total}")
        return total


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    # print(data)

    testData = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

    processes = {}

    data = data.split('\n')
    for process in data:
        split = process.split(', ')
        firstIndexSplit = split[0].split(' ')
        name, weight = firstIndexSplit[0], firstIndexSplit[1]
        p = Process(name, eval(weight))
        processes[name] = p
        subProcs = split[1:]
        if '(' not in firstIndexSplit[-1]:
            subProcs.append(firstIndexSplit[-1])

        for spName in subProcs:
            try:
                sP = processes[spName]
                p.subProcs[spName] = sP
            except KeyError:
                p.subProcs[spName] = None

    for proc in processes.values():
        for checkProc in processes.values():
            for subProcName in checkProc.subProcs.keys():
                if proc.name == subProcName and checkProc.subProcs[subProcName] is None:
                    checkProc.subProcs[subProcName] = proc

    for proc in processes.values():
        for subProc in proc.subProcs.values():
            subProc.parentProc = proc

    rootProc = None
    for proc in processes.values():
        while proc.parentProc is not None:
            proc = proc.parentProc

        rootProc = proc

    rootProc.getHoldingWeight()



starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
