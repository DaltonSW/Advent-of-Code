import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)
    rows = data.split('\n')
    total = 0
    for row in rows:
        split = row.split(' ')
        for i in range(len(split)):
            split[i] = ''.join(sorted(split[i]))
        if len(split) == len(set(split)):
            total += 1

    print(total)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
