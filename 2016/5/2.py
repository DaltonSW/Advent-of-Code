import time
import aocd
import os
from hashlib import md5


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    index = 0
    password = '########'
    while '#' in password:
        curHash = md5((data + str(index)).encode())
        hashString = curHash.hexdigest()
        if hashString[0:5] == '00000':
            print(f"{index} - {hashString}")
            if hashString[5] in ['0', '1', '2', '3', '4', '5', '6', '7']:
                place = int(hashString[5])
                if password[place] == '#':
                    password = password[:place] + hashString[6] + password[place + 1:]
        index += 1

    print(password)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
