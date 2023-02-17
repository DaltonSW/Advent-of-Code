import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    # print(data)

    IDs = data.split('\n')
    two = 0
    three = 0
    for i in range(len(IDs)):
        for j in range(i + 1, len(IDs)):
            if checkStrings(IDs[i], IDs[j]):
                print(f"{IDs[i]}\n{IDs[j]}")
                return

    print(two * three)


def checkStrings(str1, str2):
    oneWrong = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if oneWrong:
                return False
            else:
                oneWrong = True
    return True


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
