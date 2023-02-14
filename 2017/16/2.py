import copy
import os
import time
import aocd


def main():
    global starttime
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))

    moves = data.split(',')

    programs = list('abcdefghijklmnop')
    seenPrograms = [''.join(programs)]
    oneBillion = 1000000000

    for i in range(oneBillion):
        programs = doDance(programs, moves)
        stringRep = ''.join(programs)
        if stringRep in seenPrograms:
            break
        seenPrograms.append(stringRep)

    answerIndex = oneBillion % len(seenPrograms)
    print(seenPrograms[answerIndex])


def doDance(programs, moves):
    for move in moves:
        rem = move[1:]
        match move[0]:
            case 's':
                temp = []
                for _ in range(int(rem)):
                    temp.append(programs.pop())
                temp.reverse()
                programs = temp + programs
                del temp

            case 'x':
                x, y = rem.split('/')
                x, y = int(x), int(y)

                programs[x], programs[y] = programs[y], programs[x]

            case 'p':
                x, y = rem.split('/')
                x, y = programs.index(x), programs.index(y)

                programs[x], programs[y] = programs[y], programs[x]
    return programs


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))

# Submitted
# okpbefghijdcanml
# dcmljghfinpokeba
# abcdefghijklmnop
# nmafleciobjgdkph
# ocmligjnhpfdkeba
# aojnhbkidepglcmf
# mjiolbahgfncekdp
