import time
from aocd import data
import re


def main():
    print(data)
    lines = data.split('\n')
    total = 0
    for line in lines:
        matches = re.findall(r'\d', line)
        total += int(matches[0] + matches[-1])

    print(total)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
