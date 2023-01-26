import time

cities = []
allPaths = []


class Vertex:
    def __init__(self, name) -> None:
        self.name = name
        self.connections = {}

    def addConnection(self, vert, weight) -> None:
        self.connections[vert] = weight

    def getFlightCost(self, destination) -> int:
        return self.connections[destination]


def main():
    global cities

    file = open('input.txt', 'r')

    graph = {}

    for line in file.readlines():
        split = line.strip().split(' ')
        f, t, d = split[0], split[2], int(split[4])
        try:
            vert = graph[f]
        except KeyError:
            vert = Vertex(f)
            graph[f] = vert
        vert.addConnection(t, d)

        try:
            vert = graph[t]
        except KeyError:
            vert = Vertex(t)
            graph[t] = vert
        vert.addConnection(f, d)

    file.close()

    # digraph.add_weighted_edges_from(edges)
    # print(nx.shortest_path(digraph, 'Dublin', "Belfast"))

    # remaining code here
    cities = graph.keys()
    weights = []
    for city in cities:
        for dest in cities:
            if city != dest:
                printAllPaths(graph, city, dest)

    for path in allPaths:
        total = 0
        for i in range(len(path) - 1):
            start = graph[path[i]]
            weight = start.getFlightCost(path[i + 1])
            total += weight
        print(f"{' -> '.join(path)} = {total}")
        weights.append(total)

    weights.sort(reverse=True)
    print(weights[0])


def printAllPaths(graph, start, end):
    visited = []
    path = []
    printAllPathsRecur(graph, start, end, visited, path)


def printAllPathsRecur(graph, node, end, visited, path):
    global cities, allPaths

    visited.append(node)
    path.append(node)

    if node == end and len(path) == len(cities):
        allPaths.append(path.copy())
    else:
        vert: Vertex = graph[node]
        for key in vert.connections.keys():
            if key not in visited:
                printAllPathsRecur(graph, key, end, visited, path)
    path.pop()
    visited.remove(node)


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
