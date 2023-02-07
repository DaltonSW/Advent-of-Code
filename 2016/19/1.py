import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    # print(data)

    elves = []

    testing = False

    [elves.append(1) for _ in range(5 if testing else int(data))]

    totalPrez = sum(elves)

    i = 0
    while True:
        elf = elves[i]
        if elf != 0:
            target = None
            while target is None:
                j = (i + 1) % len(elves)
                while j != i:
                    if elves[j] != 0:
                        target = j
                        j = i
                    else:
                        j = (j + 1) % len(elves)
                break

            elves[i] = elf + elves[target]
            # print(f"Elf {i + 1} takes Elf {target + 1}'s {elves[target]} presents")
            if elves[i] == totalPrez:
                print(i + 1)
                break
            elves[target] = 0
        # else:
            # print(f"Elf {i + 1} has no presents and is skipped.")
        i = (i + 1) % len(elves)
        # time.sleep(.33)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
