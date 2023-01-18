import time

def main():
    f = open('input.txt', 'r')

    elves = []
    count = 0
    for line in f.readlines():
        if line=='\n':
            elves.append(count)
            count = 0
        else:
            count += int(line)
            

    f.close()

    print(max(elves))


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
