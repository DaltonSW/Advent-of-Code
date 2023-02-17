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
                fabric[sX + x][sY + y] += 1

    for claim in claims:
        if checkClaim(claim, fabric):
            print(claim)
            return


def checkClaim(claim, fabric) -> bool:
    split = claim.split(' @ ')
    nums = split[1].split(': ')
    startPos = nums[0].split(',')
    claimRange = nums[1].split('x')
    sX, sY = int(startPos[0]), int(startPos[1])
    rX, rY = int(claimRange[0]), int(claimRange[1])

    for x in range(rX):
        for y in range(rY):
            if fabric[sX + x][sY + y] > 1:
                return False

    return True


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
