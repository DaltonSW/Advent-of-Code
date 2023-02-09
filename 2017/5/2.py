import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    instructions = data.split('\n')
    for i in range(len(instructions)):
        instructions[i] = int(instructions[i])

    i = 0
    count = 0
    while len(instructions) > i > -1:
        offset = instructions[i]
        if instructions[i] > 2:
            instructions[i] -= 1
        else:
            instructions[i] += 1
        i += offset
        count += 1

    print(count)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
