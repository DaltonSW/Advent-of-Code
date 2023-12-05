import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    # print(data)

#     data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

    scoreTotal = 0
    cardNum = 0

    for card in data.split('\n'):
        cardScore = 0
        cardNum += 1
        numbers = card.split(': ')[1].split(' | ')
        winners = numbers[0].split()
        mine = numbers[1].split()

        for n in mine:
            if n in winners:
                if cardScore == 0:
                    cardScore = 1
                else:
                    cardScore *= 2

        print(f"Card {cardNum}: {cardScore}")

        scoreTotal += cardScore

    print(scoreTotal)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
