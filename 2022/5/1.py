import time


def main():
    f = open('input.txt', 'r')

    inputStacks = [f.readline(), f.readline(), f.readline(), f.readline(), f.readline(), f.readline(), f.readline(), f.readline()]
    inputStacks.reverse()
    f.readline() # numbers
    f.readline() # blank line

    stacks = [[], [], [], [], [], [], [], [], []]

    for row in inputStacks:
        tempRow = row
        for i in range(0, 9):
            block = tempRow[0:3]
            if block[1] != " ":
                stacks[i].append(block[1])
            tempRow = tempRow[4:len(tempRow)]
    
    for instruction in f.readlines():
        split = instruction.split(" ")
        qty = int(split[1])
        start = int(split[3]) - 1
        end = int(split[5]) - 1
        for i in range(qty):
            stacks[end].append(stacks[start].pop())

    f.close()
    # remaining code here
    for stack in stacks:
        print(stack.pop(), end="")
    print()


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
