import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    total = 0

    for line in data.split('\n'):
        total += checkLine(line)

    print(total)


def checkLine(line: str) -> int:
    pulls = line.split(': ')[1].split("; ")
    maxRed, maxGreen, maxBlue = 0, 0, 0
    for pull in pulls:
        colors = pull.split(', ')
        for colorInfo in colors:
            num, color = colorInfo.split(' ')
            match color:
                case 'red':
                    if int(num) > maxRed:
                        maxRed = int(num)
                case 'green':
                    if int(num) > maxGreen:
                        maxGreen = int(num)
                case 'blue':
                    if int(num) > maxBlue:
                        maxBlue = int(num)
                case _:
                    return 0
    return maxRed * maxBlue * maxGreen


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
