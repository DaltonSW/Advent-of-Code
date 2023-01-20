import time

def main():
    f = open('input.txt', 'r')

    X = 1
    cycles = []

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

    CRT = ['.'] * 240

    offset = 0
    for i in range(0, len(cycles)):
        X = cycles[i]
        spritePos = [X - 1, X, X + 1]
        if (i - offset) in spritePos:
            CRT[i] = '#'
        if (i + 1) % 40 == 0:
            offset += 40

    print(CRT[0], end='')
    for i in range(1, len(CRT)):
        if i % 40 == 0:
            print()
        print(CRT[i], end='')

    print()



starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
