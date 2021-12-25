import time


def main():
    f = open('input.txt', 'r')

    packages = f.readlines()

    f.close()

    total = 0
    for package in packages:
        l, w, h = package.split('x')
        l, w, h = int(l), int(w), int(h)
        tempTotal = (2 * l * w) + (2 * w * h) + (2 * h * l) + min(l * w, w * h, h * l)
        total += tempTotal

    print("Amount of wrapping paper needed: {} sqft".format(total))


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
