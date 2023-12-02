import time
import aocd
import os

validRed, validGreen, validBlue = 12, 13, 14


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    gameID = 0
    total = 0

    for line in data.split('\n'):
        gameID += 1
        if checkLine(line):
            total += gameID

    print(total)


def checkLine(line: str) -> bool:
    pulls = line.split(': ')[1].split("; ")
    for pull in pulls:
        colors = pull.split(', ')
        for colorInfo in colors:
            num, color = colorInfo.split(' ')
            match color:
                case 'red':
                    if int(num) > validRed:
                        return False
                case 'green':
                    if int(num) > validGreen:
                        return False
                case 'blue':
                    if int(num) > validBlue:
                        return False
                case _:
                    return True
    return True


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
