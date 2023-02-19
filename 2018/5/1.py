import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    # print(data)

    parseString = data
    # parseString = 'dabAcCaCBAcCcaDA'

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

    print(len(parseString))


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
