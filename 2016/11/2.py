import time
import aocd
import os


def main():
    numItemsPerFloor = [8, 2, 4, 0]
    print(getMoves(numItemsPerFloor))


def getMoves(items):
    """
    I found this on Reddit in the comments -- https://tinyurl.com/5dd2jp3k
    First explanation of the problem that made any damn sense on how to solve

    To move n items up 1 floor, it requires 2 * (n - 1) - 1 moves

    So assuming a "good" start state, it doesn't matter what is on what floor
    Just the number of things per floor
    """
    moves = 0
    while items[-1] != sum(items):
        lowestFloor = 0
        while items[lowestFloor] == 0:
            lowestFloor += 1
        moves += 2 * (items[lowestFloor] - 1) - 1
        items[lowestFloor + 1] += items[lowestFloor]
        items[lowestFloor] = 0
    return moves


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
