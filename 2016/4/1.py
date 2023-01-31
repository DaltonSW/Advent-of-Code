import time
import aocd
import os


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    data = data.split('\n')

    testData = [
        'aaaaa-bbb-z-y-x-123[abxyz]',
        'a-b-c-d-e-f-g-h-987[abcde]',
        'not-a-real-room-404[oarel]',
        'totally-real-room-200[decoy]'
    ]
    total = 0
    for room in data:
        split = room.split('[')
        checksum = split[1][:-1]
        roomSansChecksum = split[0].split('-')
        ID = int(roomSansChecksum.pop())
        charCount = {}
        for block in roomSansChecksum:
            for c in block:
                try:
                    charCount[c] += 1
                except KeyError:
                    charCount[c] = 1

        sortedCharCount = {k: v for k, v in sorted(charCount.items(), key=lambda item: (item[1], -ord(item[0])), reverse=True)}
        valid = True
        for i in range(4):
            try:
                if sortedCharCount[checksum[i]] > sortedCharCount[checksum[i + 1]]:
                    continue
                elif sortedCharCount[checksum[i]] == sortedCharCount[checksum[i + 1]]:
                    if ord(checksum[i + 1]) < ord(checksum[i]):
                        valid = False
                else:
                    valid = False
            except KeyError:
                valid = False
                continue
        if valid:
            total += ID

    print(total)


def sortDict(item):
    return -1 * item[1], item[0]


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
