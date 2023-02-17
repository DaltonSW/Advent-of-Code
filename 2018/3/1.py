import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    claims = data.split('\n')
    fabric = []
    for _ in range(1200):
        row = [0 for _ in range(1200)]
        fabric.append(row)

    for claim in claims:
        split = claim.split(' @ ')
        nums = split[1].split(': ')
        startPos = nums[0].split(',')
        claimRange = nums[1].split('x')
        sX, sY = int(startPos[0]), int(startPos[1])
        rX, rY = int(claimRange[0]), int(claimRange[1])

        for x in range(rX):
            for y in range(rY):
                modX, modY = sX + x, sY + y
                fabric[modX][modY] += 1

    total = 0
    for row in fabric:
        for thing in row:
            if thing > 1:
                total += 1

    print(total)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
