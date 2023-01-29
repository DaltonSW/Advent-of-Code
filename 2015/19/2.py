import time
from random import shuffle


def main():
    replacements = []
    targetMol = ''

    f = open('input.txt', 'r')

    for line in f.readlines():
        line = line.strip()
        if line != '':
            try:
                base, repl = line.split(' => ')
                replacements.append((base, repl))
            except ValueError:
                targetMol = line

    f.close()

    count = 0
    shuffles = 0
    mol = targetMol
    while len(mol) > 1:
        start = mol
        for base, repl in replacements:
            while repl in mol:
                count += mol.count(repl)
                mol = mol.replace(repl, base)

        if start == mol:
            shuffle(replacements)
            mol = targetMol
            count = 0
            shuffles += 1

    print(f"Found: {count} transforms after {shuffles} shuffles")


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
