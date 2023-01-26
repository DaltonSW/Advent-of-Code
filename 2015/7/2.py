import time


def main():
    f = open('input.txt', 'r')

    values = {}
    instructions = []

    for line in f.readlines():
        split = line.strip().split(' ')
        print(split)

        target = split[-1]
        if split[1] != "->":
            instructions.append(line.strip())
        else:
            try:
                value = int(split[0])
                values[target] = value

            except ValueError:
                instructions.append(line.strip())

    f.close()

    bitMask = 0xFFFF
    originalValues = values.copy()
    secondPass = instructions.copy()

    while len(instructions) > 0:
        instruction = instructions[0]
        split = instruction.split(' ')
        target = split[-1]
        try:
            if split[0] == "NOT":
                value = split[1]
                temp = ~values[value]
                temp = int(temp) if int(temp) > 0 else (65536 + int(temp))
                values[target] = temp
                instructions.pop(0)

            elif split[1] == "->":
                values[target] = values[split[0]]
                instructions.pop(0)
            else:
                first, second = split[0], split[2]
                first = int(first) if first.isnumeric() else values[first]
                second = int(second) if second.isnumeric() else values[second]
                match split[1]:
                    case "AND":
                        temp = (first & second) & bitMask
                    case "OR":
                        temp = (first | second) & bitMask
                    case _:
                        if split[1][0] == 'R':
                            try:
                                temp = (first >> second) & bitMask
                            except ValueError:
                                temp = (first >> second) & bitMask
                        else:
                            try:
                                temp = (first << second) & bitMask
                            except ValueError:
                                temp = (first >> second) & bitMask

                # temp = int(temp) if int(temp) > 0 else (65535 + int(temp))
                values[target] = temp
                instructions.pop(0)
        except KeyError:
            instructions.append(instruction)
            instructions.pop(0)

    # for key in values.keys():
    #    print(f"{key}: {values[key]}")

    a = values['a']
    values = originalValues
    values['b'] = a

    while len(secondPass) > 0:
        instruction = secondPass[0]
        split = instruction.split(' ')
        target = split[-1]
        try:
            if split[0] == "NOT":
                value = split[1]
                temp = ~values[value]
                temp = int(temp) if int(temp) > 0 else (65536 + int(temp))
                values[target] = temp
                secondPass.pop(0)

            elif split[1] == "->":
                values[target] = values[split[0]]
                secondPass.pop(0)
            else:
                first, second = split[0], split[2]
                first = int(first) if first.isnumeric() else values[first]
                second = int(second) if second.isnumeric() else values[second]
                match split[1]:
                    case "AND":
                        temp = (first & second) & bitMask
                    case "OR":
                        temp = (first | second) & bitMask
                    case _:
                        if split[1][0] == 'R':
                            try:
                                temp = (first >> second) & bitMask
                            except ValueError:
                                temp = (first >> second) & bitMask
                        else:
                            try:
                                temp = (first << second) & bitMask
                            except ValueError:
                                temp = (first >> second) & bitMask

                # temp = int(temp) if int(temp) > 0 else (65535 + int(temp))
                values[target] = temp
                secondPass.pop(0)
        except KeyError:
            secondPass.append(instruction)
            secondPass.pop(0)

    print(values['a'])


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
