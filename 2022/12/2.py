import time
import networkx as nx
import networkx.exception


class Vertex:
    def __init__(self, posX: int, posY: int, height: str):
        self.neighbors = []
        self.ID = hash((posX, posY))
        self.X = posX
        self.Y = posY
        if height == 'E':
            self.height = 26
        elif height == 'S':
            self.height = 1
        else:
            self.height = ord(height) - 96

    def __str__(self):
        return f"({self.X}, {self.Y} -- {self.height})"

    def __hash__(self):
        return self.ID

    def addNeighbor(self, neighbor) -> None:
        self.neighbors.append(neighbor)

    def getConnections(self) -> []:
        return self.neighbors

    def getID(self) -> int:
        return self.ID


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def __contains__(self, ID):
        return ID in self.vertList

    def addVertex(self, vertex: Vertex) -> None:
        self.numVertices += 1
        self.vertList[vertex.ID] = vertex

    def getVertex(self, ID) -> Vertex:
        return self.vertList[ID]

    def addEdge(self, f: Vertex, t: Vertex) -> None:
        if f not in self.vertList:
            self.addVertex(f)

        if t not in self.vertList:
            self.addVertex(t)

        self.vertList[f.ID].addNeighbor(t)


def main():
    f = open('input.txt', 'r')

    inputMap = []
    startingPoints = []

    for line in f.readlines():
        tempLine = []
        for c in line.strip():
            tempLine.append(c)
        inputMap.append(tempLine)

    f.close()

    # remaining code here

    # Fill graph with vertices
    graph = Graph()
    digraph = nx.DiGraph()
    for row in range(len(inputMap)):
        for col in range(len(inputMap[row])):
            height = inputMap[row][col]
            vertex = Vertex(row, col, height)
            graph.addVertex(vertex)
            digraph.add_node(vertex)
            if height == 'E':
                end = vertex
            if vertex.height == 1:
                startingPoints.append(vertex)

    for row in range(len(inputMap)):
        for col in range(len(inputMap[row])):
            baseVert = graph.getVertex(hash((row, col)))
            try:
                checkVert = graph.getVertex(hash((row - 1, col)))  # Up neighbor
                if checkVert:
                    if checkVert.height - baseVert.height < 2:
                        graph.addEdge(baseVert, checkVert)
                        digraph.add_edge(baseVert, checkVert)
            except KeyError:
                pass

            try:
                checkVert = graph.getVertex(hash((row + 1, col)))  # Down neighbor
                if checkVert:
                    if checkVert.height - baseVert.height < 2:
                        graph.addEdge(baseVert, checkVert)
                        digraph.add_edge(baseVert, checkVert)
            except KeyError:
                pass

            try:
                checkVert = graph.getVertex(hash((row, col - 1)))  # Left neighbor
                if checkVert:
                    if checkVert.height - baseVert.height < 2:
                        graph.addEdge(baseVert, checkVert)
                        digraph.add_edge(baseVert, checkVert)
            except KeyError:
                pass

            try:
                checkVert = graph.getVertex(hash((row, col + 1)))  # Right neighbor
                if checkVert:
                    if checkVert.height - baseVert.height < 2:
                        graph.addEdge(baseVert, checkVert)
                        digraph.add_edge(baseVert, checkVert)
            except KeyError:
                pass

    # path = findShortestPath(graph, graph.getVertex(hash(startPos)), graph.getVertex(hash(endPos)))
    # print(len(path))

    solutions = []
    for start in startingPoints:
        try:
            length = nx.shortest_path_length(digraph, start, end)
            print(length)
            solutions.append(length)
        except networkx.exception.NetworkXNoPath:
            continue
    solutions.sort()
    print(solutions[0])


def findShortestPath(graph: Graph, start: Vertex, end: Vertex, path=None) -> []:
    if path is None:
        path = []
    path.append(start)
    if start == end:
        return path

    try:
        graph.getVertex(start.ID)
    except KeyError:
        return None

    shortest = None
    for node in graph.getVertex(start.ID).neighbors:
        if node not in path:
            newPath = findShortestPath(graph, node, end, path)
            if newPath:
                if not shortest or len(newPath) < len(shortest):
                    shortest = newPath

    return shortest



starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
