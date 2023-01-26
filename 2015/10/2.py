import time


def main():
    puzzleInput = "1321131112"
    testInput = "1"
    var = puzzleInput

    for i in range(50):
        var = LookAndSay(var)

    # remaining code here
    print(len(var))


def LookAndSay(var):
    curCount = 0
    curDigit = -1
    output = ""
    for c in var:
        if curDigit == -1:
            curDigit = int(c)
        if int(c) != curDigit:
            output += str(curCount) + str(curDigit)
            curDigit = int(c)
            curCount = 0
        curCount += 1

    output += str(curCount) + str(curDigit)
    print(output)
    return output


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
