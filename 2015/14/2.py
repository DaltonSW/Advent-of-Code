import time


class Reindeer:
    def __init__(self, name: str, velocity: int, stamina: int, rest: int) -> None:
        self.name = name
        self.velocity = velocity
        self.flightStamina = stamina
        self.restTime = rest
        self.isResting = False
        self.timeSpentResting = 0
        self.timeSpentFlying = 0
        self.distanceTraveled = 0
        self.points = 0

    def __str__(self):
        return f"{self.name} ({self.distanceTraveled} km): {self.points}"

    def addPoint(self) -> None:
        self.points += 1

    def getPoints(self) -> int:
        return self.points

    def doTurn(self) -> None:
        if self.isResting:
            self.rest()
        else:
            self.fly()

    def rest(self) -> None:
        self.timeSpentResting += 1
        if self.timeSpentResting >= self.restTime:
            self.isResting = False
            self.timeSpentResting = 0

    def fly(self) -> None:
        self.distanceTraveled += self.velocity
        self.timeSpentFlying += 1
        if self.timeSpentFlying >= self.flightStamina:
            self.isResting = True
            self.timeSpentFlying = 0

    def getDist(self) -> int:
        return self.distanceTraveled


class Storage:
    def __init__(self) -> None:
        self.max = 0
        self.reindeer = []

    def add(self, reindeer: Reindeer) -> None:
        if reindeer.distanceTraveled > self.max:
            self.max = reindeer.distanceTraveled
            self.reindeer.clear()
            self.reindeer.append(reindeer)

        elif reindeer.distanceTraveled == self.max:
            self.reindeer.append(reindeer)

    def clear(self) -> None:
        self.max = 0
        self.reindeer = []

    def getWinners(self) -> list[Reindeer]:
        return self.reindeer


def main():
    f = open('input.txt', 'r')

    reindeer = []

    for line in f.readlines():
        split = line.strip().split(' ')
        name, vel, stamina, rest = split[0], int(split[3]), int(split[6]), int(split[13])
        reindeer.append(Reindeer(name, vel, stamina, rest))
        # parsing code here

    f.close()

    # remaining code here

    storage = Storage()

    for i in range(2503):
        storage.clear()
        for r in reindeer:
            r.doTurn()
            storage.add(r)

        for winner in storage.getWinners():
            winner.addPoint()

    for r in reindeer:
        print(r)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
