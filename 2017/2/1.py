import time
import aocd
import os
import re


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)
    nums = data.split('\n')
    checksum = 0
    for row in nums:
        n = []
        numsInRow = re.findall(r'\d+', row)
        for num in numsInRow:
            n.append(int(num))

        checksum += max(n) - min(n)

    print(checksum)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
