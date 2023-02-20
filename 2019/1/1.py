import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)
    total = 0
    nums = data.split('\n')
    for num in nums:
        temp = int(num)
        while temp > 0:
            temp = analyze(temp)
            total += temp

    print(total)


def analyze(num):
    return max(num // 3 - 2, 0)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
