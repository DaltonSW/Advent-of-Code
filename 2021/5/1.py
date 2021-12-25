import numpy, time

ARRAY_SIZE = 1000

def main():
    f = open('input.txt', 'r')
    coords = f.readlines()
    f.close()

    plot = numpy.zeros((ARRAY_SIZE, ARRAY_SIZE), dtype=int)

    for line in coords:
        splitCoords = line.split()
        x1, y1 = splitCoords[0].split(',')
        x2, y2 = splitCoords[2].split(',')

        if x1 == x2:
            plotVerticalLine(plot, int(x1), int(y1), int(y2))

        elif y1 == y2:
            plotHorizontalLine(plot, int(y1), int(x1), int(x2))

    #printPlot(plot)

    occurrences = numpy.count_nonzero(plot > 1)
    print("Cells with overlap: {}".format(occurrences))

def plotHorizontalLine(plot, y, x1, x2):
    if (x1 > x2):
        step = -1
    else:
        step = 1
    
    for i in range(x1, x2+step, step):
        plot[y][i] += 1
    return

def plotVerticalLine(plot, x, y1, y2):
    if (y1 > y2):
        step = -1
    else:
        step = 1
    
    for i in range(y1, y2+step, step):
        plot[i][x] += 1
    return

def printPlot(plot):
    for x in plot:
        for y in x:
            if y == 0:
                y = '.'
            print(y, end='')
        print('\n')

starttime = time.time()
main()
endtime = time.time()
print("Runtime: {} seconds".format(round(endtime-starttime, 3)))