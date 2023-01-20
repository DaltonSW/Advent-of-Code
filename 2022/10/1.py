import time

def main():
    f = open('input.txt', 'r')

    X = 1
    cycles = [X]

    for line in f.readlines():
        split = line.strip().split(" ")
        if split[0] == "noop":
            cycles.append(X)
        else:
            cycles.append(X)
            cycles.append(X)
            X += int(split[1])

    f.close()

    # remaining code here
    i = 20
    total = 0
    while i <= 220:
        print("{} * {} = {}".format(i, cycles[i], cycles[i] * i))
        total += cycles[i] * i
        i += 40
    print(total)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
