import time, re


def main():
    f = open('input.txt', 'r')

    words = f.readlines()

    f.close()

    print(len([s for s in words if (re.search(r'(..).*\1', s) and re.search(r'(.).\1', s))]))


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
