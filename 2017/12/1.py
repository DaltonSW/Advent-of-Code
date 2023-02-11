import time
import aocd
import os


class Program:
    def __init__(self, num: int, connections: [int]):
        self.num = num
        self.connections = connections


count = 0
programs = {}


def main():
    global count, programs
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)
    programDefs = data.split('\n')

    for progDef in programDefs:
        num, connections = progDef.split(' <-> ')
        num = int(num)
        connections = connections.split(', ')
        connections = [int(x) for x in connections]
        newProg = Program(num, connections)
        programs[num] = newProg

    analyzeProg(programs[0], [programs[0]])

    print(count)


def analyzeProg(program: Program, visited: list[Program]):
    global count, programs

    count += 1

    for connectionNum in program.connections:
        connection = programs[connectionNum]
        if connection not in visited:
            visited.append(connection)
            analyzeProg(connection, visited)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
