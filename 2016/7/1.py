import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    data = data.split('\n')
    # print(data)

    testData = [
        'abba[mnop]qrst',
        'abcd[bddb]xyyx',
        'aaaa[qwer]tyui',
        'ioxxoj[asdfgh]zxcvbn'
    ]

    IPs = []

    for string in data:
        if checkString(string):
            IPs.append(string)

    print(len(IPs))


def checkString(checkInput: str) -> bool:

    firstSplit = checkInput.split('[')
    wholeSplit = []
    outerResults = []
    for block in firstSplit:
        block = block.split(']')
        for item in block:
            wholeSplit.append(item)

    for idx, check in enumerate(wholeSplit):
        for i in range(len(check) - 3):
            a1, b1, b2, a2 = check[i], check[i+1], check[i+2], check[i+3]
            if a1 == b1 or a2 == b2:
                continue
            elif a1 == a2 and b1 == b2:
                if idx % 2 == 0:
                    outerResults.append(True)
                else:
                    return False

    return True in outerResults


starttime = time.time()
main()
endtime = time.time()




print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
