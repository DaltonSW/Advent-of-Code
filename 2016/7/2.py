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
        if checkStringForSSL(string):
            IPs.append(string)

    print(len(IPs))


def checkStringForSSL(checkInput: str) -> bool:
    firstSplit = checkInput.split('[')
    wholeSplit = []
    outsideBracketStrings = []
    insideBracketStrings = []
    for block in firstSplit:
        block = block.split(']')
        for item in block:
            wholeSplit.append(item)

    for idx, string in enumerate(wholeSplit):
        if idx == 0:
            outsideBracketStrings.append(string)
            continue
        elif idx % 2 == 0:
            outsideBracketStrings.append(string)
        else:
            insideBracketStrings.append(string)

    for outer in outsideBracketStrings:
        for i in range(len(outer) - 2):
            a1, b1, a2 = outer[i], outer[i+1], outer[i+2]
            if a1 != b1 and a1 == a2:
                for inner in insideBracketStrings:
                    for j in range(len(inner) - 2):
                        B1, A1, B2 = inner[j], inner[j + 1], inner[j + 2]
                        if B1 == b1 and B2 == b1 and A1 == a1:
                            return True



def checkStringForTLS(checkInput: str) -> bool:

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
