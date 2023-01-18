import time

LETTERS = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def main():
    f = open('input.txt', 'r')

    commons = []

    for line in f.readlines():
        mid = int(len(line) / 2)
        firstHalf = line[0:mid]
        secHalf = line[mid:len(line)]
        print("{} -- {}".format(firstHalf, secHalf))
        for c in firstHalf:
            if c in secHalf:
                commons.append(c)
                break

    f.close()

    # remaining code here
    print(commons)
    total = 0
    for c in commons:
        total += LETTERS.index(c)

    print(total)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
