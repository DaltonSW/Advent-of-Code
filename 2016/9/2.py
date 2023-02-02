import time
import aocd
import os
import re


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    # testData = [
    #     '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN',
    #     '(6x1)(1x3)A',
    #     'X(8x2)(3x3)ABCY',
    #     '(27x12)(20x12)(13x14)(7x10)(1x12)A',
    # ]
    #
    # for data in testData:
    #     print(f"{data} -> {analyze(data)}")

    print(analyze(data))


def analyze(data: str):
    answer = ''
    normalChars = 0
    multChars = 0
    while len(data) > 0:
        c = data[0]
        if c != '(':
            answer += c
            normalChars += 1
            data = data[1:]
        else:
            parenIndex = data.find(')')
            params = data[1:parenIndex]
            data = data[parenIndex + 1:]
            chars, times = params.split('x')
            substring = data[:int(chars)]
            data = data[int(chars):]
            if '(' not in substring:
                normalChars += int(chars) * int(times)
                for _ in range(int(times)):
                    answer += substring
            else:
                multChars += int(times) * analyze(substring)

    return normalChars + multChars


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
