import time
import aocd
import os
import re


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)
    digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    replacements = ["zero", "o1e", "t2o", "th3ee", "f4ur", "f5ve", "s6x", "se7en", "ei8ht", "ni9e"]
    for i in range(1, 10):
        data = data.replace(digits[i], replacements[i])
    print(data)
    lines: list[str] = data.split('\n')
    total = 0
    for line in lines:
        firstNum, lastNum = -1, -1
        for c in line:
            if c.isnumeric():
                if firstNum == -1:
                    firstNum = c
                lastNum = c
        total += int(firstNum + lastNum)

    print(total)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
