import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)
    nums = data.split('\n')
    total = 0
    for n in nums:
        total += int(n)

    print(total)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
