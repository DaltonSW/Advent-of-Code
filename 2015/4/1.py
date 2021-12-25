import time, hashlib


def main():
    puzzleInput = 'ckczppom'

    # remaining code here
    num = -1
    while True:
        num += 1
        init = puzzleInput + str(num)
        hashed = hashlib.md5(init.encode('utf-8')).hexdigest()
        if hashed[0:5] == '00000':
            break

    print("First accepted number: {}".format(num))


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
