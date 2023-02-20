import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    testData = '1,9,10,3,2,3,11,0,99,30,40,50'
    for n in range(100):
        for v in range(100):
            if tryValues(n, v, data) == 19690720:
                print(100 * n + v)
                return


def tryValues(noun, verb, data):
    ints = data.split(',')
    ints = [int(x) for x in ints]
    i = 0
    ints[1] = noun
    ints[2] = verb
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

    return ints[0]


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
