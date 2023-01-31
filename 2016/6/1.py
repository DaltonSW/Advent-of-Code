import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    data = data.split('\n')

    # f = open('test.txt', 'r')
    # data = []
    # for line in f.readlines():
    #     data.append(line.strip())
    # f.close()

    dicts = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    for row in data:
        for i in range(1, 9):
            addOrIncChar(dicts[i], row[i - 1])

    for d in dicts:
        if d == {}:
            continue
        sortedChars = list({k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)})
        print(sortedChars[0])
    print(data)


def addOrIncChar(dictionary: dict, char: str):
    try:
        dictionary[char] += 1
    except KeyError:
        dictionary[char] = 1

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
