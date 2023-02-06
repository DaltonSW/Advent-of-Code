import time
import aocd
import os
import hashlib
import re

hashes = []
keys = []


def main():
    global hashes, keys
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    for i in range(50000):
        key = f"{data}{i}"
        # key = f"abc{i}"
        md5 = hashlib.md5(key.encode())
        hashes.append(md5.hexdigest())

    for i, h in enumerate(hashes):
        if checkHash(h, i) and h not in keys:
            keys.append(h)
            print(f"{h} -- {i}")
            if len(keys) == 64:
                print(i)
                return


def checkHash(h: str, index: int) -> bool:
    global hashes, keys
    for i in range(len(h) - 2):
        if h[i] == h[i + 1] and h[i] == h[i + 2]:
            return checkFutureHash(index, h[i])


def checkFutureHash(index: int, char: str) -> bool:
    global hashes

    for i in range(index + 1, index + 1001):
        h = hashes[i]
        if re.search(char + "{5,}", h) is not None:
            print(f"\tQuintuplet Found -- {h} -- {i}")
            return True

    return False


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
