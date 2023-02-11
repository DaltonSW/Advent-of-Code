import time
import aocd
import os


class Program:
    def __init__(self, num: int, connections: [int]):
        self.num = num
        self.connections = connections

    def __lt__(self, other):
        return self.num > other.num

count = 0
programs = {}
groups = []
currentGroup = []


def main():
    global count, programs, groups
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)
    programDefs = data.split('\n')

    testDefs = [
        '0 <-> 2',
        '1 <-> 1',
        '2 <-> 0, 3, 4',
        '3 <-> 2, 4',
        '4 <-> 2, 3, 6',
        '5 <-> 6',
        '6 <-> 4, 5'
    ]

    for progDef in programDefs:
        num, connections = progDef.split(' <-> ')
        num = int(num)
        connections = connections.split(', ')
        connections = [int(x) for x in connections]
        newProg = Program(num, connections)
        programs[num] = newProg

    for i in range(len(programs)):
        curProg = programs[i]
        curGroup = analyzeProg(curProg, [curProg])
        curGroup.sort()
        if curGroup not in groups:
            groups.append(curGroup)

    print(len(groups))


def analyzeProg(program: Program, visited: list[Program]):
    global count, programs, groups, currentGroup

    for connectionNum in program.connections:
        connection = programs[connectionNum]
        if connection not in visited:
            visited.append(connection)
            analyzeProg(connection, visited)

    return visited


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
