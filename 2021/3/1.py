from bit import Bit 

def main():
    storage = []
    for z in range(12):
        storage.append(Bit())

    f = open('input.txt', 'r')

    initArray = f.readlines()

    f.close()

    for line in initArray:
        for i in range(len(line)-1):
            if line[i] == '1':
                storage[i].ones += 1

            else:
                storage[i].zeroes += 1

    gamma = ""
    for index in storage:
        print("Zeroes: {} - Ones: {}".format(index.zeroes, index.ones))
        if index.zeroes > index.ones:
            gamma += '0'
        else:
            gamma += '1'

    print("Gamma: {} - {}".format(gamma, int(gamma, 2)))

    epsilon = ""
    for num in gamma:
        if num == '0':
            epsilon += '1'
        else:
            epsilon += '0'

    print("Epsilon: {} - {}".format(epsilon, int(epsilon, 2)))

    print("Power Consumption: {}".format(int(gamma, 2) * int(epsilon, 2)))


main()

