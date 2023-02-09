import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = int(aocd.get_data(None, int(cwd[-1]), int(cwd[-2])))
    print(data)

    prevHighest = 1
    numRings = 1
    i = 0

    while True:
        numRings += 1
        prevHighest += i * 4
        i += 2
        print(f"{numRings} - {prevHighest} - {prevHighest - i // 2 + 1}")
        if prevHighest > data:
            break

    # I did it by hand after I got these values figured out.
    # My input is on the bottom of its square, so I calc'd the distance from
    # it to the center column, and then added the number of squares that
    # had been generated (AKA number of columns to go up)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
