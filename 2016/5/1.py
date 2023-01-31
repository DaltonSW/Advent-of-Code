import time
import aocd
import os
from hashlib import md5


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    index = 0
    password = ''
    while len(password) < 8:
        curHash = md5((data + str(index)).encode())
        hashString = curHash.hexdigest()
        if hashString[0:5] == '00000':
            password += hashString[5]
            print(f"{index} - {hashString}")
        index += 1

    print(password)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
