import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)
    curDir = 0
    curPlace = [0, 0]
    directions = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]
    ]

    visitedPlaces = []

    for item in data.strip().split(', '):
        match item[0]:
            case 'L':
                curDir = (curDir - 1) % 4
            case 'R':
                curDir = (curDir + 1) % 4
        movement = int(item[1:])
        direction = directions[curDir]
        for i in range(movement):
            curPlace = [curPlace[0] + direction[0], curPlace[1] + direction[1]]
            if curPlace in visitedPlaces:
                print(curPlace)
                print(curPlace[0] + curPlace[1])
                return
            else:
                visitedPlaces.append(curPlace)
                print(f"{item} - {curPlace}")

    print(curPlace[0] + curPlace[1])


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
