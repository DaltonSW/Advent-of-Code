import time


def main():
    f = open('input.txt', 'r')

    packages = f.readlines()

    f.close()

    total = 0
    for package in packages:
        l, w, h = package.split('x')
        l, w, h = int(l), int(w), int(h)
        sides = [l, w, h]
        sides.remove(max(sides))
        tempTotal = (2 * sum(sides)) + (l * w * h)
        total += tempTotal

    print("Amount of ribbon needed: {} feet".format(total))


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
