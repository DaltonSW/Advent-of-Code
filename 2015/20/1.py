import time


def main():
    goal = 36000000
    curNum = 0
    while True:
        curNum += 1
        houseTotal = 0
        divs = getDivisors(curNum)
        for div in divs.keys():
            houseTotal += div * 10

        # print(f"House {curNum} got {houseTotal} presents")
        if curNum % 10000 == 0:
            print(curNum)

        if houseTotal >= goal:
            print(curNum)
            break


def getDivisors(num: int) -> dict:
    divs = {}
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divs[i] = 1
            divs[num // i] = 1
    return divs


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
