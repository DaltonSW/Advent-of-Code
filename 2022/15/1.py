import time


class Sensor:
    def __init__(self, x: int, y: int, bX: int, bY: int) -> None:
        self.x = x
        self.y = y
        self.beaconX = bX
        self.beaconY = bY
        self.manhattan = abs(x - bX) + abs(y - bY)

    def __str__(self):
        return f"({self.x}, {self.y}) --> ({self.beaconX}, {self.beaconY})"


def main():
    inputFile = 'input.txt'
    f = open(inputFile, 'r')

    sensors = []
    beacons = []

    for line in f.readlines():
        splitLine = line.strip().split(' ')
        sensorX = splitLine[2].split('=')
        sensorX = int(sensorX[1][:-1])  # Remove the comma

        sensorY = splitLine[3].split('=')
        sensorY = int(sensorY[1][:-1])  # Remove the colon

        beaconX = splitLine[8].split('=')
        beaconX = int(beaconX[1][:-1])  # Remove the comma

        beaconY = splitLine[9].split('=')
        beaconY = int(beaconY[1])

        sensors.append(Sensor(sensorX, sensorY, beaconX, beaconY))
        if (beaconX, beaconY) not in beacons:
            beacons.append((beaconX, beaconY))

    f.close()

    # remaining code here

    row = 10 if inputFile == 'test.txt' else 2000000
    spaces = {}
    for sensor in sensors:
        print(f"Analyzing sensor: {sensor}")
        heightDiff = abs(sensor.y - row)
        slack = sensor.manhattan - heightDiff
        for i in range(-slack, slack + 1):
            space = (sensor.x + i, row)
            if space not in beacons:
                spaces[space] = 1

    print(len(spaces))


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))

# calc distance
# find diff between sensor's Y and row we're interested in
# difference in distance between (sensor and beacon) and (sensor and row)
#  > this represents how many "slack" squares there are on either side of the sensor's X
#  > add em all to a list, then remove dupes, then count
