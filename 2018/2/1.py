import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    IDs = data.split('\n')
    two = 0
    three = 0
    for ID in IDs:
        thisTwo = False
        thisThree = False
        for c in ID:
            if ID.count(c) == 2 and not thisTwo:
                thisTwo = True
                two += 1
            elif ID.count(c) == 3 and not thisThree:
                thisThree = True
                three += 1

    print(two * three)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
