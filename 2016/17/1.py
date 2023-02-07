import hashlib
import time
import aocd
import os

successes = []
unlocked = ['b', 'c', 'd', 'e', 'f']


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    testing = False
    testData = [
        'ihgpwlah',
        'kglvqrro',
        'ulqzkmiv'
    ]

    if testing:
        for password in testData:
            tryExits(password)
            print(min(successes, key=len))
            successes.clear()

    else:
        tryExits(data)
        print(min(successes, key=len))


def tryExits(password: str, path: str = '', curRoom: (int, int) = (0, 0)):
    global successes, unlocked

    if curRoom == (3, 3):
        successes.append(path)
        return

    md5 = hashlib.md5(password.encode()).hexdigest()

    if md5[0] in unlocked:
        nextRoom = (curRoom[0] - 1, curRoom[1])
        if nextRoom[0] >= 0:
            tryExits(password + 'U', path + 'U', nextRoom)

    if md5[1] in unlocked:
        nextRoom = (curRoom[0] + 1, curRoom[1])
        if nextRoom[0] <= 3:
            tryExits(password + 'D', path + 'D', nextRoom)

    if md5[2] in unlocked:
        nextRoom = (curRoom[0], curRoom[1] - 1)
        if nextRoom[1] >= 0:
            tryExits(password + 'L', path + 'L', nextRoom)

    if md5[3] in unlocked:
        nextRoom = (curRoom[0], curRoom[1] + 1)
        if nextRoom[1] <= 3:
            tryExits(password + 'R', path + 'R', nextRoom)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
