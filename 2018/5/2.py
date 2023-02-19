import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    # print(data)

    parseString = data
    results = []

    for i in range(65, 91):
        tempStr = ''
        for c in parseString:
            if ord(c) == i or ord(c) == i + 32:
                continue
            else:
                tempStr += c
        results.append(react(tempStr))

    print(min(results))


def react(parseString) -> int:
    madeSwap = True
    while madeSwap:
        tempStr = ''
        madeSwap = False
        i = 0
        while i < len(parseString) - 1:
            if abs(ord(parseString[i]) - ord(parseString[i + 1])) == 32:
                i += 2
                madeSwap = True
            else:
                tempStr += parseString[i]
                i += 1

        parseString = tempStr + parseString[-1]

    return len(tempStr) + 1


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
