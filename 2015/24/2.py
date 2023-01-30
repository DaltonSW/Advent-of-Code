from itertools import combinations
from functools import reduce
import time

allOptions = []


def main():
    global allOptions
    packages = []
    f = open('input.txt', 'r')

    for line in f.readlines():
        packages.append(int(line.strip()))
    f.close()

    totalWeight = sum(packages)
    goalWeight = totalWeight // 4

    fittingQEs = []

    for i in range(len(packages)):
        for combo in combinations(packages, i):
            if sum(combo) == goalWeight:
                fittingQEs.append(reduce(lambda a, b: a * b, combo))

    print(min(fittingQEs))



starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
