import time


def main():
    curPassword = "cqjxxyzz"
    curPassword = incrementPassword(curPassword)

    while True:
        if testPassword(curPassword):
            print(curPassword)
            return
        else:
            curPassword = incrementPassword(curPassword)


def incrementPassword(password) -> str:
    passwordInts = []
    [passwordInts.append(ord(x)) for x in password]

    for i in range(len(passwordInts) - 1, -1, -1):
        temp = passwordInts[i] + 1
        if temp < 123:
            output = ''
            for c in passwordInts[:-1]:
                output += chr(c)
            return output + chr(temp)
        else:
            passwordInts[i] = ord('a')
            passwordInts[i-1] += 1
            if all(test < 123 for test in passwordInts):
                output = ''
                for c in passwordInts:
                    output += chr(c)
                return output


def testPassword(password) -> bool:
    if 'i' in password or 'o' in password or 'l' in password:
        return False

    straightCheck = []
    pairOne = []
    pairTwo = []

    hasStraight = False
    onePair = False
    twoPair = False

    passwordInts = []
    [passwordInts.append(ord(x)) for x in password]

    for i in range(len(passwordInts)):
        c = passwordInts[i]
        if len(straightCheck) == 0:
            straightCheck.append(c)
        else:
            if straightCheck[-1] == c - 1:
                straightCheck.append(c)
                if len(straightCheck) == 3:
                    hasStraight = True
            else:
                straightCheck.clear()
                straightCheck.append(c)

        if len(pairOne) == 0:
            pairOne.append(c)

        elif not onePair:
            if c == pairOne[0]:
                pairOne.append(c)
                onePair = True
                continue

            else:
                pairOne[0] = c

        if len(pairOne) == 2 and len(pairTwo) == 0:
            pairTwo.append(c)

        else:
            if len(pairTwo) == 0:
                continue
            elif c == pairTwo[0]:
                pairTwo.append(c)
                twoPair = True
                continue
            else:
                pairTwo[0] = c

    return hasStraight and onePair and twoPair


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
