import time
import aocd
import os
import re


def main():
    data = """Time:        51699878
Distance:   377117112241505"""

    timeLimit, recordDist = 51699878, 377117112241505
    waysToWin = 0
    for ms in range(timeLimit + 1):
        if ms * (timeLimit - ms) > recordDist:
            waysToWin += 1
    print(waysToWin)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
