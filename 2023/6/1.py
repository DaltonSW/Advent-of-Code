import time
import aocd
import os
import re


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))

#     data = """Time:      7  15   30
# Distance:  9  40  200"""
    print(data)

    times, distances = data.split('\n')

    times = re.findall('\\d+', times)
    distances = re.findall('\\d+', distances)

    wins = []

    for i in range(len(times)):
        timeLimit, recordDist = int(times[i]), int(distances[i])
        waysToWin = 0
        for ms in range(timeLimit + 1):
            if ms * (timeLimit - ms) > recordDist:
                waysToWin += 1
        wins.append(waysToWin)

    total = 1
    for w in wins:
        total *= w
    print(total)

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
