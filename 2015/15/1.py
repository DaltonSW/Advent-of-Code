import time


class Ingredient:
    def __init__(self, split: list) -> None:
        self.name = split[0][:-1]
        self.capacity = int(split[2])
        self.durability = int(split[4])
        self.flavor = int(split[6])
        self.texture = int(split[8])
        self.calories = int(split[10])


def main():
    f = open('input.txt', 'r')
    output = open('output.txt', 'w')

    ingredients = []

    for line in f.readlines():
        split = line.strip().replace(',', '').split(' ')
        ingredients.append(Ingredient(split))
        print(line)
        # parsing code here

    f.close()

    # remaining code here

    best = 0

    for i in range(4):
        for w in range(100, 0, -1):
            for x in range(100 - w, -1, -1):
                for y in range(100 - w - x, -1, -1):
                    z = 100 - w - x - y
                    one, two, three, four = ingredients[i], ingredients[(i + 1) % 4], ingredients[(i + 2) % 4], ingredients[(i + 3) % 4]
                    capacity = max(w * one.capacity + x * two.capacity + y * three.capacity + z * four.capacity, 0)
                    dur = max(w * one.durability + x * two.durability + y * three.durability + z * four.durability, 0)
                    flavor = max(w * one.flavor + x * two.flavor + y * three.flavor + z * four.flavor, 0)
                    texture = max(w * one.texture + x * two.texture + y * three.texture + z * four.texture, 0)
                    result = capacity * dur * flavor * texture
                    if result != 0:
                        print(f"{w} tsp {one.name}, {x} tsp {two.name}, {y} tsp {three.name}, {z} tsp {four.name}: {result}")
                    output.write(f"{w} tsp {one.name}, {x} tsp {two.name}, {y} tsp {three.name}, {z} tsp {four.name}: {result}\n")
                    output.write(f"\t{w} * {one.capacity} + {x} * {two.capacity} + {y} * {three.capacity} + {z} * {four.capacity} = {capacity}\n")
                    output.write(f"\t{w} * {one.durability} + {x} * {two.durability} + {y} * {three.durability} + {z} * {four.durability} = {dur}\n")
                    output.write(f"\t{w} * {one.flavor} + {x} * {two.flavor} + {y} * {three.flavor} + {z} * {four.flavor} = {flavor}\n")
                    output.write(f"\t{w} * {one.texture} + {x} * {two.texture} + {y} * {three.texture} + {z} * {four.texture} = {texture}\n")
                    if result > best:
                        best = result

    print(best)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
