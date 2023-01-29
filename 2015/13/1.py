import time
from itertools import permutations


class Person:
    def __init__(self, name: str) -> None:
        self.name = name
        self.feelings = {}

    def addFeelings(self, name: str, num: int) -> None:
        self.feelings[name] = num

    def getFeeling(self, name: str) -> int:
        return self.feelings[name]


def main():
    f = open('input.txt', 'r')

    people = {}

    for line in f.readlines():
        split = line.strip().split(' ')
        name = split[0]
        try:
            person = people[name]
        except KeyError:
            person = Person(name)
            people[name] = person

        feelingNum = int(split[3])
        feelingNum *= -1 if split[2] == 'lose' else 1
        feelingName = split[-1][:-1]
        person.addFeelings(feelingName, feelingNum)
        # parsing code here
    f.close()

    # remaining code here
    bestHappiness = 0
    perms = list(permutations(people))
    for perm in perms:
        totalHappiness = 0
        for i in range(len(perm) - 1):
            person = people[perm[i]]
            totalHappiness += person.getFeeling(perm[i + 1])

        for i in range(1, len(perm)):
            person = people[perm[i]]
            totalHappiness += person.getFeeling(perm[i - 1])

        totalHappiness += people[perm[0]].getFeeling(perm[-1])
        totalHappiness += people[perm[-1]].getFeeling(perm[0])

        if totalHappiness > bestHappiness:
            bestHappiness = totalHappiness
        print(f"{perm} -- {totalHappiness}")

    print(bestHappiness)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
