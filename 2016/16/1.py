import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    testing = False

    diskLength = 272 if not testing else 20
    data = data if not testing else '10000'

    while len(data) < diskLength:
        data = processString(data)

    data = data[:diskLength]
    check = data
    while True:
        check = checksum(check)
        if len(check) % 2 != 0:
            print(check)
            return


def processString(value: str) -> str:
    swapped = ''
    for c in value:
        swapped += '1' if c == '0' else '0'

    answer = value + '0' + swapped[::-1]
    print(f"Processed: {answer}")

    return answer


def checksum(value: str) -> str:
    answer = ''
    for i in range(0, len(value), 2):
        answer += '1' if value[i] == value[i+1] else '0'

    print(f"Checksum: {answer}")
    return answer


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
