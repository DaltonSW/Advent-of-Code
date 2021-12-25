import time

def main():
    f = open('input.txt', 'r')

    initPos = f.readline().split(',')

    f.close()

    choices = []

    for i in range(len(initPos)):
        choices.append(sum([abs(int(pos) - i) for pos in initPos]))
    print(min(choices))

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime-starttime, 3)))