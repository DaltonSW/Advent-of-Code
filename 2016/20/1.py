import time
import aocd
import os


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

    for IP in range(10 if testing else 2**32 + 1):
        if checkIP(IP, testRanges if testing else ranges):
            print(f"Found {IP}")
            return


def checkIP(IP: int, ranges: [(int, int)]) -> bool:
    for r in ranges:
        if IP > r[1]:
            continue
        if IP >= r[0]:
            return False
        return True


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
