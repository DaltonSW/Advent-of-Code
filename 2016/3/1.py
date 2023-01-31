import time
import aocd
import os
import re


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    data = data.split('\n')
    possible = 0
    for line in data:
        numbers = re.findall(r'\d+', line)
        print(numbers)
        if int(numbers[0]) + int(numbers[1]) > int(numbers[2]) and int(numbers[1]) + int(numbers[2]) > int(numbers[0]) and int(numbers[2]) + int(numbers[0]) > int(numbers[1]):
            possible += 1

    print(possible)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
