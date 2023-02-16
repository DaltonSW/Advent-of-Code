import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)
    nums = data.split('\n')
    seen = {}
    total = 0
    i = 0
    while True:
        n = nums[i]
        total += int(n)
        if total in seen:
            print(total)
            return
        else:
            seen[total] = 1
            i = (i + 1) % len(nums)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
