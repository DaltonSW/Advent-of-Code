from bit import Bit
from enum import Enum
import copy

class Direction(Enum):
    LEAST_COMMON = 0
    MOST_COMMON = 1

def main():
    f = open('input.txt', 'r')
    initArray = f.readlines()
    f.close()

    oxygenArray = copy.deepcopy(initArray)
    carbonArray = copy.deepcopy(initArray)

    oxygenArray = filter(oxygenArray, Direction.MOST_COMMON)
    carbonArray = filter(carbonArray, Direction.LEAST_COMMON)

    print("Oxygen Rating: {} - {}".format(oxygenArray[0], int(oxygenArray[0], 2)))
    print("Carbon Rating: {} - {}".format(carbonArray[0], int(carbonArray[0], 2)))
    print("Product: {}".format(int(oxygenArray[0], 2) * int(carbonArray[0], 2)))



def count(arr, storage):    
    for bit in storage:
        bit.clear()

    for line in arr:
        for i in range(len(line)-1):
            if line[i] == '1':
                storage[i].ones += 1

            else:
                storage[i].zeroes += 1

def filter(arr, direction):
    storage = []
    for z in range(12):
        storage.append(Bit())

    for index in range(len(arr[0])):
        count(arr, storage)
        # Check storage[index] to see which is the bigger value
        # Go through arr and remove any values that don't contain the bigger value there

        if direction == Direction.MOST_COMMON:
            if storage[index].ones >= storage[index].zeroes:
                remainder = '1'
            else:
                remainder = '0'

        else:
            if storage[index].ones < storage[index].zeroes:
                remainder = '1'
            else:
                remainder = '0'

        arr = [num for num in arr if num[index]==remainder]

        if len(arr)==1:
            return arr

main()

