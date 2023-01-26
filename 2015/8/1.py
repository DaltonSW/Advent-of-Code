import time
import re


def main():
    f = open('input.txt', 'r')
    total = 0

    for line in f.readlines():
        line = line.strip()
        val = 2 + line.count("\\") + line.count('"')
        total += val

    f.close()

    # remaining code here

    print(total)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
