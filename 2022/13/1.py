import ast
import time


class Packet:
    def __init__(self, left: str, right: str, index: int):
        self.left = ast.literal_eval(left)
        self.right = ast.literal_eval(right)
        self.index = index


def main():
    f = open('input.txt', 'r')

    packets = []
    line = "temp"

    while line != '':
        left = f.readline()  # First packet
        right = f.readline()  # Second packet
        line = f.readline()  # Either blank line or EOF

        packet = Packet(left, right, len(packets) + 1)
        packets.append(packet)
    f.close()

    # remaining code here

    total = 0
    for packet in packets:
        total += analyze(packet) * packet.index
        print()
    print(total)


def analyze(packet: Packet, left=None, right=None, tabs=0) -> int:
    tabStr = '\t' * tabs
    if left is None or right is None:
        left = packet.left
        right = packet.right
        print(f"== Pair {packet.index} ==")
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
            val = analyze(packet, l, r, tabs + 1)
            if val == -1:
                continue

            return val

        if isinstance(l, int):
            l = [l]
            print(f"{tabStr}\t- Mixed types; convert left to {l} and retry comparison")

        if isinstance(r, int):
            r = [r]
            print(f"{tabStr}\t- Mixed types; convert left to {r} and retry comparison")

        val = analyze(packet, l, r, tabs + 1)
        if val == -1:
            continue

        return val

    return -1  # If both items were the same


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
