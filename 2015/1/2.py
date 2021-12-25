import time


def main():
    f = open('input.txt', 'r')

    parens = f.readline().strip()

    f.close()

    floor = 0

    for idx, char in enumerate(parens):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor <= 0:
            print("Entered basement on instruction {}".format(idx+1))
            break

    print("Floor: {}".format(floor))


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
