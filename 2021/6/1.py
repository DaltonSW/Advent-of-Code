import time

TOTAL_DAYS = 80

def main():
    f = open('input.txt', 'r')

    initNumbers = f.readline().split(',')

    f.close()

    fishList = []

    for num in initNumbers:
        fishList.append(int(num))

    print("Total Fish: {}".format(len(fishList)))

    for i in range(1, TOTAL_DAYS+1):
        newFish = []
        for index, fish in enumerate(fishList):
            if fish == 0:
                fishList[index] = 6
                newFish.append(8)
            else:
                fishList[index] -= 1
        fishList = fishList + newFish
        print("Fish after {} days: {}".format(i, len(fishList)))

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime-starttime, 3)))