import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    testData = [
        'b inc 5 if a > 1',
        'a inc 1 if b < 5',
        'c dec -10 if a >= 1',
        'c inc -20 if c == 10'
    ]

    registers = {}

    highestEver = 0

    instructions = data.split('\n')
    for wholeInst in instructions:
        split = wholeInst.split(' if ')
        target, inst, num = split[0].split(' ')
        checkTarg, comp, val = split[1].split(' ')
        executeInst = False
        try:
            _ = registers[checkTarg]
        except KeyError:
            registers[checkTarg] = 0

        match comp:
            case '<=':
                if registers[checkTarg] <= int(val):
                    executeInst = True
                else:
                    executeInst = False
            case '>=':
                if registers[checkTarg] >= int(val):
                    executeInst = True
                else:
                    executeInst = False
            case '==':
                if registers[checkTarg] == int(val):
                    executeInst = True
                else:
                    executeInst = False
            case '<':
                if registers[checkTarg] < int(val):
                    executeInst = True
                else:
                    executeInst = False
            case '>':
                if registers[checkTarg] > int(val):
                    executeInst = True
                else:
                    executeInst = False
            case '!=':
                if registers[checkTarg] != int(val):
                    executeInst = True
                else:
                    executeInst = False

        if executeInst:
            try:
                mult = -1 if inst == 'dec' else 1
                registers[target] += int(num) * mult
            except KeyError:
                registers[target] = 0
                mult = -1 if inst == 'dec' else 1
                registers[target] += int(num) * mult
            if registers[target] > highestEver:
                highestEver = registers[target]

    print(highestEver)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
