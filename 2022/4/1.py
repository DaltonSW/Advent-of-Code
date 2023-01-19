import time

def main():
    f = open('input.txt', 'r')

    total = 0
    for line in f.readlines():
        line = line.strip('\n')
        one, two = line.split(",")
        oneStart, oneEnd = one.split("-")
        twoStart, twoEnd = two.split("-")
        oneRange = range(int(oneStart), int(oneEnd) + 1)
        twoRange = range(int(twoStart), int(twoEnd) + 1)

        valid = True
        for i in oneRange:
            if i not in twoRange:
                valid = False
                break
        if valid:
            total += 1
            
        else:
            valid = True
            for i in twoRange:
                if i not in oneRange:
                    valid = False
                    break
            if valid:
                total += 1
                

    f.close()

    # remaining code here
    print(total)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
