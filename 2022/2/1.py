import time
from enum import Enum

class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Outcome(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6


def main():
    f = open('input.txt', 'r')

    total = 0
    for line in f.readlines():
        oppChoice = line[0]
        myChoice = line[2]
        match myChoice:
            case "X":
                choice = Choice.ROCK
                match oppChoice:
                    case "A":
                        outcome = Outcome.DRAW
                    case "B":
                        outcome = Outcome.LOSS
                    case "C":
                        outcome = Outcome.WIN
            case "Y":
                choice = Choice.PAPER
                match oppChoice:
                    case "A":
                        outcome = Outcome.WIN
                    case "B":
                        outcome = Outcome.DRAW
                    case "C":
                        outcome = Outcome.LOSS
            case "Z":
                choice = Choice.SCISSORS
                match oppChoice:
                    case "A":
                        outcome = Outcome.LOSS
                    case "B":
                        outcome = Outcome.WIN
                    case "C":
                        outcome = Outcome.DRAW
        total += choice.value + outcome.value

    f.close()

    print(total)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
