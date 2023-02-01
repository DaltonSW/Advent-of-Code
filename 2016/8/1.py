import time
import aocd
import os
import numpy

def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    data = data.split('\n')

    matrix = []
    for _ in range(6):
        matrixRow = ['.'] * 50
        matrix.append(matrixRow)

    for command in data:
        split = command.split(' ')
        match split[0]:
            case 'rect':
                cols, rows = split[1].split('x')
                for r in range(int(rows)):
                    for c in range(int(cols)):
                        matrix[r][c] = '#'

            case 'rotate':
                amount = int(split[-1])
                index = int(split[2].split('=')[1])
                match split[1]:
                    case 'row':
                        row = matrix[index]
                        matrix[index] = numpy.roll(row, amount)

                    case 'column':
                        transArr = numpy.array(matrix).T
                        col = transArr[index]
                        transArr[index] = numpy.roll(col, amount)
                        matrix = numpy.array(transArr).T.tolist()

    total = 0
    for row in matrix:
        for cell in row:
            if cell == '#':
                total += 1
            print(cell, end='')
        print()

    print(total)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
