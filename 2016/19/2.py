import time
from datetime import timedelta
import aocd
import os
from collections import deque


class Node:
    def __init__(self, num):
        self.num = num
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self, headNode):
        self.head = headNode

    def addNode(self, node):
        n = self.head
        if n.next is None:
            n.next = node
            n.prev = node
            node.next = n
            node.prev = n
        else:
            n = n.prev
            n.next = node
            node.prev = n
            node.next = self.head
            self.head.prev = node


def main():
    cwd = os.getcwd().split('\\')
    numElves = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))

    testing = False
    numElves = 5 if testing else int(numElves)

    linkedList = LinkedList(Node(1))
    for i in range(2, numElves + 1):
        linkedList.addNode(Node(i))

    elf = linkedList.head
    target = elf
    for _ in range(numElves // 2):
        target = target.next

    moveTwo = False

    while elf.next != elf:
        p = target.prev
        n = target.next
        p.next = n
        n.prev = p

        elf = elf.next
        target = target.next
        if moveTwo:
            target = target.next
        moveTwo = not moveTwo

    print(elf.num)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
