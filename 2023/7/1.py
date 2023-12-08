import time
import aocd
import os
import re
import functools
from enum import Enum
from collections import Counter

cardValues = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13
}

class HandRank(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

@functools.total_ordering
class Hand:
    def __init__(self, hand):
        temp = hand.split()
        self.cards: list[str] = [c for c in temp[0]]
        self.bet: int = int(temp[1])
        self.rank: HandRank = self.EvaluateRank()

    def EvaluateRank(self) -> HandRank:
        if len(set(self.cards)) == 5:  # If they're all different...
            return HandRank.HIGH_CARD
        elif len(set(self.cards)) == 1:  # Or all the same
            return HandRank.FIVE_OF_A_KIND

        ranks = Counter(self.cards)

        if 4 in ranks.values():
            return HandRank.FOUR_OF_A_KIND

        if set(ranks.values()) == {2, 3}:
            return HandRank.FULL_HOUSE

        elif 3 in ranks.values():
            return HandRank.THREE_OF_A_KIND

        if list(ranks.values()).count(2) == 2:
            return HandRank.TWO_PAIR
        elif list(ranks.values()).count(2) == 1:
            return HandRank.ONE_PAIR

        return HandRank.HIGH_CARD

    def __str__(self):
        return f"Cards: {self.cards} ({self.rank.name}), Bet: {self.bet}"

    def __lt__(self, other):
        if self.rank != other.rank:
            return self.rank.value < other.rank.value
        for i in range(len(self.cards)):
            if cardValues[self.cards[i]] != cardValues[other.cards[i]]:
                return cardValues[self.cards[i]] < cardValues[other.cards[i]]


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    # print(data)

#     data = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""

    hands = [Hand(hand) for hand in data.split('\n')]

    hands.sort()

    for hand in hands:
        print(hand)

    total = 0
    for i in range(len(hands)):
        scoreRank = i + 1
        hand = hands[i]
        total += hand.bet * scoreRank

    print(total)

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
