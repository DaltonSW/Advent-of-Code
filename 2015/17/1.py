import time
import itertools

def main():
    f = open('input.txt', 'r')

    containers = []
    solutions = []

    for line in f.readlines():
        containers.append(int(line.strip()))
        # parsing code here

    f.close()

    # remaining code here

    for i in range(len(containers)):
        for s in itertools.combinations(containers, i):
            if sum(s) == 150:
                solutions.append(s)

    print(len(solutions))


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
