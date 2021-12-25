import time

def main():
    f = open('input.txt', 'r')

    initRead = f.readline()

    f.close()

    positions = [int(x) for x in initRead.split(',')]

    choices = []

    print("Total positions to check: {}".format(max(positions)))
    time.sleep(1)
    # looping through each possible horizontal between 0 and max offset to get all possibilities (probably not efficient)
    for i in range(max(positions)):
        start = time.time()
        # each index in diffs has distance between pos and i
        diffs = [abs(pos - i) for pos in positions]
        totalFuel = 0
        for diff in diffs:
            totalFuel += sum(list(range(diff+1)))
        choices.append(totalFuel)
        print("Total Fuel to move everyone to index {}: {} ({}s)".format(i, totalFuel, round(time.time()-start, 2)))
    print("Cheapest amount of fuel spent is {} by moving to position {}".format(min(choices), choices.index(min(choices))))

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime-starttime, 3)))