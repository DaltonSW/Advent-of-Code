import time
import aocd
import os
from collections import deque


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    data = data.split('\n')

    ranges = []

    testRanges = [(5, 8), (0, 2), (4, 7)]

    for r in data:
        s, e = r.split('-')
        ranges.append((int(s), int(e)))

    ranges.sort()
    testRanges.sort()

    testing = False

    ranges = deque(ranges)

    total = 0
    IP = 0
    while IP < 2**32:
        result, IP = checkIP(IP, ranges)
        if result:
            print(f"Found {IP}")
            total += 1
        else:
            ranges.popleft()
        IP += 1

    print(total)
    return


def checkIP(IP: int, ranges) -> (bool, int):
    for r in ranges:
        if IP > r[1]:
            continue
        if IP >= r[0]:
            return False, r[1]
        return True, IP


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
