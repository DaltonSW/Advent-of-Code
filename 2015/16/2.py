import time


class Aunt:
    def __init__(self, ID: int):
        self.ID = ID
        self.children = -1
        self.cats = -1
        self.samoyeds = -1
        self.pomeranians = -1
        self.akitas = -1
        self.vizslas = -1
        self.goldfish = -1
        self.trees = -1
        self.cars = -1
        self.perfumes = -1

    def addAttribute(self, attr: str, num: int):
        match attr:
            case "children":
                self.children = num
            case "cats":
                self.cats = num
            case "samoyeds":
                self.samoyeds = num
            case "pomeranians":
                self.pomeranians = num
            case "akitas":
                self.akitas = num
            case "vizslas":
                self.vizslas = num
            case "goldfish":
                self.goldfish = num
            case "trees":
                self.trees = num
            case "cars":
                self.cars = num
            case "perfumes":
                self.perfumes = num

    def getAttribute(self, attr: str) -> int:
        match attr:
            case "children":
                return self.children
            case "cats":
                return self.cats
            case "samoyeds":
                return self.samoyeds
            case "pomeranians":
                return self.pomeranians
            case "akitas":
                return self.akitas
            case "vizslas":
                return self.vizslas
            case "goldfish":
                return self.goldfish
            case "trees":
                return self.trees
            case "cars":
                return self.cars
            case "perfumes":
                return self.perfumes


def main():
    equalProps = ['children', 'samoyeds', 'akitas', 'vizslas', 'cars', 'perfumes']
    lessThanProps = ['pomeranians', 'goldfish']
    moreThanProps = ['cats', 'trees']

    f = open('input.txt', 'r')

    aunts = []

    realSue = Aunt(0)
    realSue.addAttribute("children", 3)
    realSue.addAttribute("cats", 7)
    realSue.addAttribute("samoyeds", 2)
    realSue.addAttribute("pomeranians", 3)
    realSue.addAttribute("akitas", 0)
    realSue.addAttribute("vizslas", 0)
    realSue.addAttribute("goldfish", 5)
    realSue.addAttribute("trees", 3)
    realSue.addAttribute("cars", 2)
    realSue.addAttribute("perfumes", 1)

    for line in f.readlines():
        line = line.strip().replace(',', '').replace(':', '')
        split = line.split(' ')
        sue = Aunt(int(split[1]))
        sue.addAttribute(split[2], int(split[3]))
        sue.addAttribute(split[4], int(split[5]))
        sue.addAttribute(split[6], int(split[7]))

        aunts.append(sue)
        # parsing code here

    f.close()

    # remaining code here

    badAunts = []
    for aunt in aunts:
        akitas = aunt.getAttribute("akitas")
        vizslas = aunt.getAttribute("vizslas")
        if akitas > 0 or vizslas > 0:
            badAunts.append(aunt)

    for aunt in badAunts:
        if aunt in aunts:
            aunts.remove(aunt)

    badAunts.clear()

    # First pass: 211 left

    for aunt in aunts:
        for prop in equalProps:
            val = aunt.getAttribute(prop)
            if val != -1 and val != realSue.getAttribute(prop):
                badAunts.append(aunt)
                break

    for aunt in badAunts:
        if aunt in aunts:
            aunts.remove(aunt)

    badAunts.clear()

    for aunt in aunts:
        for prop in lessThanProps:
            val = aunt.getAttribute(prop)
            if val != -1 and not val < realSue.getAttribute(prop):
                badAunts.append(aunt)
                break

    for aunt in badAunts:
        if aunt in aunts:
            aunts.remove(aunt)

    badAunts.clear()

    for aunt in aunts:
        for prop in moreThanProps:
            val = aunt.getAttribute(prop)
            if val != -1 and not val > realSue.getAttribute(prop):
                badAunts.append(aunt)
                break

    for aunt in badAunts:
        if aunt in aunts:
            aunts.remove(aunt)

    badAunts.clear()

    print(aunts[0].ID)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
