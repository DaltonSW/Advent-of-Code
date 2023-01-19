import time

def main():
    f = open('input.txt', 'r')

    line = f.readline()
    buffer = []
    for i in range(len(line)):
        curChar = line[i]
        if i in range(0, 13):
            buffer.append(curChar)
        else:
            buffer.append(curChar)
            if checkBuffer(buffer):
                print(i + 1)
                return
            else:
                buffer = buffer[1:]

    f.close()

    # remaining code here
    

def checkBuffer(buffer):
    for i in range(0, 14):
        char = buffer[i]
        for j in range(i + 1, 14):
            if buffer[j] == char:
                print("{} - False".format(buffer))
                return False
    print("{} - True".format(buffer))
    return True

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
