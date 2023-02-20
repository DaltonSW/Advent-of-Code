import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    testData = '1,9,10,3,2,3,11,0,99,30,40,50'

    ints = data.split(',')
    ints = [int(x) for x in ints]
    i = 0
    ints[1] = 12
    ints[2] = 2
    while i < len(ints):
        opcode = ints[i]
        if opcode != 99:
            posOne = ints[i+1]
            posTwo = ints[i+2]
            outPos = ints[i+3]
        match opcode:
            case 1:
                ints[outPos] = ints[posOne] + ints[posTwo]
                i += 4

            case 2:
                ints[outPos] = ints[posOne] * ints[posTwo]
                i += 4

            case 99:
                i = len(ints) + 1

    print(ints[0])


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
