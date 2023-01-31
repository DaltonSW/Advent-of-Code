import time
import aocd
import os
import re


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    data = data.split('\n')
    possible = 0
    triangles = []
    for i in range(0, len(data), 3):
        line1, line2, line3 = data[i], data[i + 1], data[i + 2]
        row1 = re.findall(r'\d+', line1)
        row2 = re.findall(r'\d+', line2)
        row3 = re.findall(r'\d+', line3)
        triangles.append((row1[0], row2[0], row3[0]))
        triangles.append((row1[1], row2[1], row3[1]))
        triangles.append((row1[2], row2[2], row3[2]))

    for numbers in triangles:
        if int(numbers[0]) + int(numbers[1]) > int(numbers[2]) and int(numbers[1]) + int(numbers[2]) > int(numbers[0]) and int(numbers[2]) + int(numbers[0]) > int(numbers[1]):
            possible += 1

    print(possible)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
