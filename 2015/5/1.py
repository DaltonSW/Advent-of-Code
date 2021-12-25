import time


def main():
    f = open('input.txt', 'r')

    words = f.readlines()

    f.close()

    # remaining code here

    niceWords = 0
    for word in words:
        if checkVowels(word) and checkDouble(word) and checkArbitrary(word):
            niceWords += 1

    print("Found this many nice words: {}".format(niceWords))


def checkArbitrary(word):
    strings = ['ab', 'cd', 'pq', 'xy']
    for thing in strings:
        if thing in word:
            return False
    return True


def checkDouble(word):
    for i in range(len(word)-2):
        if word[i] == word[i+1]:
            return True
    return False


def checkVowels(word):
    numVowels = 0
    for char in word:
        if char in ['a', 'e', 'i', 'o', 'u']:
            numVowels += 1
            if numVowels == 3:
                return True

    return False

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
