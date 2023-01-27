import time
import re
import json


def main():
    f = open('input.txt', 'r')
    line = f.readline()
    jsonObj = json.loads(line)
    f.close()

    print(analyze(jsonObj))


def analyze(item) -> int:
    temp = 0
    if isinstance(item, dict):
        for value in item.values():
            if value == 'red':
                return 0
            elif isinstance(value, int):
                temp += value
            elif not isinstance(value, str):
                temp += analyze(value)

    elif isinstance(item, list):
        for i in item:
            if isinstance(i, int):
                temp += i
            elif not isinstance(i, str):
                temp += analyze(i)

    elif isinstance(item, int):
        temp = item

    elif isinstance(item, str):
        temp = 0

    return temp



starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
