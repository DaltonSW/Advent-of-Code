import time, hashlib


def main():
    puzzleInput = 'ckczppom'

    # remaining code here
    num = -1
    loopStart = time.time()
    while True:
        num += 1
        init = puzzleInput + str(num)
        hashed = hashlib.md5(init.encode('utf-8')).hexdigest()
        if num % 1000000 == 0:
            print("Reached {} -- ({})".format(num, round(time.time() - loopStart, 3)))
        if hashed[0:6] == '000000':
            break

    print("First accepted number: {}".format(num))


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
