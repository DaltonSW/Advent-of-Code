import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    testData = [
        '<>',
        '<random characters>',
        '<<<<>',
        '<{!>}>',
        '<!!>',
        '<!!!>>',
        '<{o"i!a,<{i<a>'
    ]

    i = 0
    depth = 0
    totalScore = 0
    isGarbage = False
    totalGarbage = 0
    while i < len(data):
        c = data[i]
        if c == '!':
            data = data[:i + 1] + data[i + 2:]

        if c not in '!' and isGarbage:
            totalGarbage += 1

        if c == '{' and not isGarbage:
            depth += 1
            totalScore += depth

        elif c == '}' and not isGarbage:
            depth -= 1

        elif c == '<' and not isGarbage:
            isGarbage = True

        elif c == '>' and isGarbage:
            isGarbage = False
            totalGarbage -= 1

        i += 1

    print(totalGarbage)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
