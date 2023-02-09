import time
import aocd
import os
import re


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    # print(data)
    nums = data.split('\n')
    checksum = 0

    testData = '''5 9 2 8
                    9 4 7 3
                    3 8 6 5'''
    for row in nums:
        n = []
        numsInRow = re.findall(r'\d+', row)
        for i in range(len(numsInRow)):
            num = int(numsInRow[i])
            for j in range(i + 1, len(numsInRow)):
                num2 = int(numsInRow[j])
                if num % num2 == 0:
                    print(f"{num} {num2}")
                    checksum += num // num2
                    break

                elif num2 % num == 0:
                    print(f"{num2} {num}")
                    checksum += num2 // num
                    break

    print(checksum)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
