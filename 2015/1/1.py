import time


def main():
    f = open('input.txt', 'r')

    parens = f.readline().strip()

    f.close()

    floor = 0

    for char in parens:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

    print("Floor: {}".format(floor))


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
