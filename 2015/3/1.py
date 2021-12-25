import time, numpy

GRID_SIZE = 300


def main():
    f = open('input.txt', 'r')

    directions = f.readline()

    f.close()

    grid = numpy.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    santa = [int(GRID_SIZE / 2), int(GRID_SIZE / 2)]
    grid[santa[0], santa[1]] += 1
    for arrow in directions:
        if arrow == '^':
            santa[1] -= 1
        if arrow == '>':
            santa[0] += 1
        if arrow == '<':
            santa[0] -= 1
        if arrow == 'v':
            santa[1] += 1
        grid[santa[0], santa[1]] += 1

    answer = 0
    for y in grid:
        for x in y:
            if x > 0:
                answer += 1

    print("Houses with more than 2 presents: {}".format(answer))


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
