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
                outcome = Outcome.LOSS
                match oppChoice:
                    case "A":
                        choice = Choice.SCISSORS
                    case "B":
                        choice = Choice.ROCK
                    case "C":
                        choice = Choice.PAPER
            case "Y":
                outcome = Outcome.DRAW
                match oppChoice:
                    case "A":
                        choice = Choice.ROCK
                    case "B":
                        choice = Choice.PAPER
                    case "C":
                        choice = Choice.SCISSORS
            case "Z":
                outcome = Outcome.WIN
                match oppChoice:
                    case "A":
                        choice = Choice.PAPER
                    case "B":
                        choice = Choice.SCISSORS
                    case "C":
                        choice = Choice.ROCK
        total += choice.value + outcome.value

    f.close()

    print(total)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
