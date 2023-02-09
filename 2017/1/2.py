import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    testData = [
        '1212',
        '1221',
        '123425',
        '123123',
        '12131415'
    ]

    total = 0
    for i in range(len(data)):
        if int(data[i]) == int(data[(i + len(data) // 2) % len(data)]):
            total += int(data[i])

    print(total)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
