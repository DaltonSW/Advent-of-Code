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

    def getPos(self) -> (int, int, int):
        return self.x, self.y, self.z


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    print(data)

    particles = []

    timeSinceCollisions = 0

    for line in data.split('\n'):
        pos, vel, acc = line.split(', ')
        particles.append(Particle(pos, vel, acc))

    while True:
        for p in particles:
            p.update()

        toBeRemoved = {}
        for i in range(len(particles)):
            particle = particles[i]
            for j in range(i + 1, len(particles)):
                if particle.getPos() == particles[j].getPos():
                    toBeRemoved[particle] = 1
                    toBeRemoved[particles[j]] = 1

        if len(toBeRemoved) == 0:
            timeSinceCollisions += 1
            if timeSinceCollisions == 100:
                print(len(particles))
                return

        else:
            for p in toBeRemoved.keys():
                particles.remove(p)
            timeSinceCollisions = 0


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
