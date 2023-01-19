import time


def main():
    f = open('input.txt', 'r')

    matrix = []
    for _ in range(2500):
        matrix.append([0] * 2500)

    headPos = [1200, 1200]
    posArray = []
    for i in range(10):
        posArray.append(headPos)

    for line in f.readlines():
        direction, amount = line.strip().split(" ")
        match direction:
            case "U":
                moveX, moveY = [-1, 0]

            case "L":
                moveX, moveY = [0, -1]

            case "D":
                moveX, moveY = [1, 0]

            case "R":
                moveX, moveY = [0, 1]

            case _:
                moveX, moveY = [0, 0]

        for i in range(int(amount)):
            headPos = posArray[0]
            posArray[0] = [headPos[0] + moveX, headPos[1] + moveY]
            for j in range(1, len(posArray)):
                following = posArray[j - 1]
                follower = posArray[j]
                posArray[j] = moveKnot(following, follower)
                if j == 9:
                    matrix[follower[0]][follower[1]] = 1

        # print("{} {} = [{}, {}] -> [{}, {}]".format(distance, direction, headX, headY, headPos[0], headPos[1]))

    f.close()

    # remaining code here
    total = 0
    for x in matrix:
        for y in x:
            total += y
    print(total + 1)  # IDK why it doesn't register visiting the final spot, but that's the way it goes


def moveKnot(headPos, tailPos) -> [int, int]:
    headX, headY = headPos[0], headPos[1]
    tailX, tailY = tailPos[0], tailPos[1]
    diff = [headX - tailX, headY - tailY]
    if abs(diff[0]) < 2 and abs(diff[1]) < 2:  # If tail and head are touching
        return tailPos
    elif diff[0] == -2 and diff[1] == 0:  # 2 up
        moveX, moveY = [-1, 0]
    elif diff[0] == 2 and diff[1] == 0:  # 2 down
        moveX, moveY = [1, 0]
    elif diff[0] == 0 and diff[1] == -2:  # 2 left
        moveX, moveY = [0, -1]
    elif diff[0] == 0 and diff[1] == 2:  # 2 right
        moveX, moveY = [0, 1]
    else:
        moveX = -1 if diff[0] < 0 else 1
        moveY = -1 if diff[1] < 0 else 1

    return [tailX + moveX, tailY + moveY]


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
