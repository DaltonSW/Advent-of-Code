import time
import re

class Mapping:
    def __init__(self, base: str) -> None:
        self.base = base
        self.replacements = []

    def addReplacement(self, repl: str):
        self.replacements.append(repl)

    def getReplacements(self) -> list[str]:
        return self.replacements

    def getBase(self) -> str:
        return self.base


def main():
    replacements = {}

    f = open('input.txt', 'r')

    for line in f.readlines():
        line = line.strip()
        if line != '':
            try:
                base, repl = line.split(' => ')
                try:
                    baseObj = replacements[base]
                except KeyError:
                    baseObj = Mapping(base)
                    replacements[base] = baseObj

                baseObj.addReplacement(repl)
            except ValueError:
                origMolecule = line
        print(line)
        # parsing code here

    f.close()

    outputs = {}
    for baseObj in replacements.values():
        for repl in baseObj.getReplacements():
            base = baseObj.getBase()
            for match in re.finditer(base, origMolecule):
                replaceStr = origMolecule[0:match.start()] + repl + origMolecule[match.end():]
                try:
                    outputs[replaceStr] += 1
                except KeyError:
                    outputs[replaceStr] = 1

    print(outputs)
    print(len(outputs))


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
