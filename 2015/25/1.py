import time


goalRow, goalCol = 2947, 3029


def main():
    inputCode = 20151125
    goal = (2947, 3029)
    code, index = inputCode, (1, 1)
    while True:
        code, index = getNextCode(code, index[0], index[1])
        if index == goal:
            print(f"Here's the code! -- {code}")
            return


def getNextCode(curCode: int, curRow: int, curCol: int) -> (int, (int, int)):
    nextCode = curCode * 252533
    nextCode %= 33554393
    nextRow = curRow - 1
    if nextRow == 0:
        nextRow = curCol + 1
        nextCol = 1
    else:
        nextCol = curCol + 1

    return nextCode, (nextRow, nextCol)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
