import time

TOTAL_DAYS = 256

def main():
    f = open('input.txt', 'r')

    initNumbers = f.readline().split(',')

    f.close()

    fishList = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for num in initNumbers:
        fishList[int(num)] += 1

    print("Total Fish: {}".format(sum(fishList)))

    for i in range(1, TOTAL_DAYS+1):
        daystart = time.time()
        temp = fishList[0]
        fishList[0] = fishList[1]
        fishList[1] = fishList[2]
        fishList[2] = fishList[3]
        fishList[3] = fishList[4]
        fishList[4] = fishList[5]
        fishList[5] = fishList[6]
        fishList[6] = fishList[7] + temp
        fishList[7] = fishList[8]
        fishList[8] = temp
        dayend = time.time()
        print("Fish after {} days: {} ({}s)".format(i, sum(fishList), round(dayend-daystart, 3)))

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime-starttime, 3)))