import time

BIG_TOTAL = 0


class File:
    name: str
    size: int

    def __init__(self, size: int, name: str) -> None:
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name: str) -> None:
        self.name = name
        self.totalSize = 0
        self.subDirs = []
        self.files = []

    def addDir(self, newDir) -> None:
        self.subDirs.append(newDir)

    def addFile(self, newFile: File) -> None:
        self.files.append(newFile)

    def calcSize(self) -> int:
        tempCalc = 0
        for file in self.files:
            tempCalc += int(file.size)

        for subDir in self.subDirs:
            tempCalc += subDir.calcSize()

        self.totalSize = tempCalc
        return self.totalSize

    def printout(self, indent: int):
        print('\t' * indent, end="")
        print("- {} (dir)".format(self.name))
        for subDir in self.subDirs:
            subDir.printout(indent + 1)
        print(self.files)

        # for file in self.files:
        #    print('\t' * (indent + 1), end="")
        #    print("- {} (file, size={})".format(file.name, file.size))


def main():
    cwd = []

    # f = open('./2022/7/test.txt.txt', 'r')
    f = open('input.txt', 'r')
    # f = open('test.txt.txt', 'r')

    f.readline()
    cwd.append(Directory("/"))
    for line in f.readlines():
        split = line.split(" ")
        if split[0] == "$":
            match split[1]:
                case "cd":
                    dirName = split[2].strip()
                    if dirName == "..":
                        cwd.pop()
                    else:
                        curDir: Directory = cwd.pop()
                        for possibleDir in curDir.subDirs:
                            if possibleDir.name == dirName:
                                cwd.append(curDir)
                                cwd.append(possibleDir)

                case "ls":
                    continue
        else:  # Something being listed out
            curDir: Directory = cwd.pop()
            # print("Current dir: {}".format(curDir.name))
            match split[0]:
                case "dir":
                    newDir = Directory(split[1].strip())
                    curDir.addDir(newDir)
                case _:
                    newFile = File(split[0].strip(), split[1].strip())
                    curDir.addFile(newFile)
            cwd.append(curDir)

    f.close()

    # remaining code here
    printout(cwd[0], 0)
    print(BIG_TOTAL)


def printout(directory: Directory, indent: int):
    global BIG_TOTAL
    print('\t' * indent, end="")
    print("- {} (dir {})".format(directory.name, directory.calcSize()))

    if directory.totalSize <= 100000:
        BIG_TOTAL += directory.totalSize

    for subDir in directory.subDirs:
        printout(subDir, indent + 1)

    for file in directory.files:
        print('\t' * (indent + 1), end="")
        print("- {} (file, size={})".format(file.name, file.size))


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
