import ast
import time


class PacketPair:
    def __init__(self, left: [], right: [], index: int = 0):
        self.left = left
        self.right = right
        self.index = index


def main():
    f = open('input.txt', 'r')

    packets = []
    packetPairs = []
    line = "temp"

    while line != '':
        left = ast.literal_eval(f.readline())  # First packet
        right = ast.literal_eval(f.readline())  # Second packet
        line = f.readline()  # Either blank line or EOF

        packetPair = PacketPair(left, right, len(packetPairs) + 1)
        packetPairs.append(packetPair)
        packets.append(left)
        packets.append(right)
    f.close()

    # remaining code here

    # total = 0
    # for packetPair in packetPairs:
    #     total += analyze(packetPair) * packetPair.index
    #     print()
    # print(total)

    packets.append(ast.literal_eval("[[2]]"))
    packets.append(ast.literal_eval("[[6]]"))
    for i in range(len(packets)):
        for j in range(len(packets) - i - 1):
            pair = PacketPair(packets[j], packets[j + 1])
            val = analyze(pair)
            if val == 0:
                packets[j], packets[j + 1] = packets[j + 1], packets[j]

    for packet in packets:
        print(packet)

    firstDiv = packets.index(ast.literal_eval("[[2]]")) + 1
    secondDiv = packets.index(ast.literal_eval("[[6]]")) + 1
    print(f'{firstDiv} * {secondDiv} = {firstDiv * secondDiv}')


def analyze(packetPair: PacketPair, left=None, right=None, tabs=0) -> int:
    tabStr = '\t' * tabs
    if left is None or right is None:
        left = packetPair.left
        right = packetPair.right
        print(f"== Pair {packetPair.index} ==")
    print(f"{tabStr}- Compare {left} vs {right}")
    for i in range(max(len(left), len(right))):
        try:
            l = left[i]
        # Left side ran out of items first
        except IndexError:
            print("\t- Left side ran out of items, so inputs are in the right order")
            return 1
        try:
            r = right[i]
        # Right side ran out of items first
        except IndexError:
            print("\t- Right side ran out of items, so inputs are not in the right order")
            return 0

        # Both items are integers
        if isinstance(l, int) and isinstance(r, int):
            print(f"{tabStr}\t- Compare {l} vs {r}")
            if l == r:
                continue

            if l < r:
                print(f"{tabStr}\t\t- Left side is smaller, so inputs are in the right order")
                return 1

            else:
                print(f"{tabStr}\t\t- Right side is smaller, so inputs are not in the right order")
                return 0

        # Both items are lists
        if isinstance(l, list) and isinstance(r, list):
            val = analyze(packetPair, l, r, tabs + 1)
            if val == -1:
                continue

            return val

        if isinstance(l, int):
            l = [l]
            print(f"{tabStr}\t- Mixed types; convert left to {l} and retry comparison")

        if isinstance(r, int):
            r = [r]
            print(f"{tabStr}\t- Mixed types; convert left to {r} and retry comparison")

        val = analyze(packetPair, l, r, tabs + 1)
        if val == -1:
            continue

        return val

    return -1  # If both items were the same


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
