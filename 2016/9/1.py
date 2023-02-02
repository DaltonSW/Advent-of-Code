import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    answer = ""

    # testData = [
    #     'ADVENT',
    #     'A(1x5)BC',
    #     '(3x3)XYZ',
    #     'A(2x2)BCD(2x2)EFG',
    #     '(6x1)(1x3)A',
    #     'X(8x2)(3x3)ABCY'
    # ]

    while len(data) > 0:
        c = data[0]
        if c != '(':
            answer += c
            data = data[1:]
        else:
            parenIndex = data.find(')')
            params = data[1:parenIndex]
            data = data[parenIndex + 1:]
            chars, times = params.split('x')
            substring = data[:int(chars)]
            data = data[int(chars):]
            for _ in range(int(times)):
                answer += substring
    print(f"{answer} - {len(answer)}")


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
