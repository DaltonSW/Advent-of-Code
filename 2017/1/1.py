import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    total = 0
    for i in range(len(data) - 1):
        if int(data[i]) == int(data[i + 1]):
            total += int(data[i])

    if int(data[-1]) == int(data[0]):
        total += int(data[-1])

    print(total)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
