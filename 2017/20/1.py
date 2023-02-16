import time
import aocd
import os


class Particle:
    def __init__(self, pos, vel, acc):
        posSplit = pos[3:-1].split(',')
        velSplit = vel[3:-1].split(',')
        accSplit = acc[3:-1].split(',')

        self.x = int(posSplit[0])
        self.y = int(posSplit[1])
        self.z = int(posSplit[2])

        self.xV = int(velSplit[0])
        self.yV = int(velSplit[1])
        self.zV = int(velSplit[2])

        self.xA = int(accSplit[0])
        self.yA = int(accSplit[1])
        self.zA = int(accSplit[2])

    def update(self):
        self.xV += self.xA
        self.yV += self.yA
        self.zV += self.zA

        self.x += self.xV
        self.y += self.yV
        self.z += self.zV

    def getManDist(self) -> int:
        return abs(self.x) + abs(self.y) + abs(self.z)


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    particles = []

    smallestParticle = -1
    timeBeenSmallest = 0

    for line in data.split('\n'):
        pos, vel, acc = line.split(', ')
        particles.append(Particle(pos, vel, acc))

    for _ in range(1000000):
        for p in particles:
            p.update()

        smallest = [9999999, -1]
        for i in range(len(particles)):
            dist = particles[i].getManDist()
            if dist < smallest[0]:
                smallest = [dist, i]

        if smallest[1] == smallestParticle:
            timeBeenSmallest += 1
            if timeBeenSmallest >= 1000:
                print(smallestParticle)
                return
        else:
            smallestParticle = smallest[1]
            timeBeenSmallest = 0


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
