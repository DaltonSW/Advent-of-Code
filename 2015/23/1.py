import time


def main():
    instructions = []
    a, b = 0, 0

    f = open('input.txt', 'r')

    for line in f.readlines():
        instructions.append(line.strip())
    f.close()

    i = 0
    while i < len(instructions):
        instruction = instructions[i].split(' ')
        print(f"Executing: {instruction}")
        match instruction[0]:
            case 'hlf':
                match instruction[1]:
                    case 'a':
                        a = a // 2
                    case 'b':
                        b = b // 2
                i += 1
            case 'tpl':
                match instruction[1]:
                    case 'a':
                        a = a * 3
                    case 'b':
                        b = b * 3
                i += 1
            case 'inc':
                match instruction[1]:
                    case 'a':
                        a += 1
                    case 'b':
                        b += 1
                i += 1
            case 'jmp':
                i += int(instruction[1])
            case 'jie':
                match instruction[1]:
                    case 'a,':
                        if a % 2 == 0:
                            i += int(instruction[2])
                            continue
                    case 'b,':
                        if b % 2 == 0:
                            i += int(instruction[2])
                            continue
                i += 1
            case 'jio':
                match instruction[1]:
                    case 'a,':
                        if a == 1:
                            i += int(instruction[2])
                            continue
                    case 'b,':
                        if b == 1:
                            i += int(instruction[2])
                            continue
                i += 1

    print((a, b))

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
