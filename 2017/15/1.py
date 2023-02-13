import time

bigNumber = 2147483647


class Generator:
    def __init__(self, start, mult):
        self.start = start
        self.mult = mult
        self.current = start

    def newNumber(self) -> int:
        global bigNumber
        self.current = (self.current * self.mult) % bigNumber
        return self.current


def main():

    startGenA = 277
    startGenB = 349

    testStartGenA = 65
    testStartGenB = 8921

    multGenA = 16807
    multGenB = 48271

    genA = Generator(startGenA, multGenA)
    testGenA = Generator(testStartGenA, multGenA)

    genB = Generator(startGenB, multGenB)
    testGenB = Generator(testStartGenB, multGenB)

    # genA = testGenA
    # genB = testGenB

    totalProcessed = 0
    totalMatches = 0
    while totalProcessed < 40000000:
        batchA = []
        batchB = []
        while len(batchA) < 100:
            batchA.append(genA.newNumber())
            batchB.append(genB.newNumber())

        # Start thread to call function (or just call it. Maybe both, see if threading actually helps at all)
        matches = processBatches(batchA, batchB)
        totalMatches += matches
        totalProcessed += 100

        batchA.clear()
        batchB.clear()

    print(totalMatches)


def processBatches(batchA: [int], batchB: [int]) -> int:
    matches = 0
    for i in range(len(batchA)):
        a = batchA[i]
        b = batchB[i]
        binA, binB = bin(a)[2:].zfill(32), bin(b)[2:].zfill(32)
        binA = binA[::-1]
        binB = binB[::-1]
        if checkPair(binA, binB):
            matches += 1

    return matches


def checkPair(a: str, b: str) -> bool:
    for i in range(16):
        if a[i] != b[i]:
            return False
    return True


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
