class Ship():
    depth = 0
    pos = 0
    aim = 0

    def move(self, dir, num):
        if dir=="forward":
            self.pos += num
            self.depth += (num * self.aim)
        elif dir=="down":
            self.aim += num
        elif dir=="up":
            self.aim -= num

    def __str__(self):
        return "Depth: {} - Position: {} -- Product: {}".format(self.depth, self.pos, (self.depth * self.pos))


def main():
    f = open('./input.txt', 'r')
    boat = Ship()
    for line in f.readlines():
        arr = line.split()
        boat.move(arr[0], int(arr[1]))

    print(boat)
    f.close()

main()
    