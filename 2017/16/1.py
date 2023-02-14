import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))

    testing = False

    data = 's1,x3/4,pe/b' if testing else data

    print(data)

    moves = data.split(',')

    programs = []
    for i in range(5 if testing else 16):
        programs.append(chr(97 + i))

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

    print(''.join(programs))

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
