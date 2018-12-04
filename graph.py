
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, item):
        return item in self.vertList

    def addEdge(self, v1, v2, cost=0):
        if v1 not in self.vertList:
            self.addVertex(v1)
        if v2 not in self.vertList:
            self.addVertex(v2)
        self.vertList[v1].addNeighbor(self.vertList[v2], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


g = Graph()
for i in range(6):
    g.addVertex(i)

print(g.vertList)

g.addEdge(0, 1, 5)
g.addEdge(0, 5, 2)
g.addEdge(1, 2, 4)
g.addEdge(2, 3, 9)
g.addEdge(3, 4, 7)
g.addEdge(3, 5, 3)
g.addEdge(4, 0, 1)
g.addEdge(5, 4, 8)
g.addEdge(5, 2, 1)

for v in g:
    for w in v.getConnections():
        print("(%s, %s)" % (v.getId(), w.getId()))



# Word Lader Graph
# from pythonds.graphs import Graph
#
# def buildGraph(wordFile):
#     d = {}
#     g = Graph()
#     wfile = open(wordFile,'r')
#     # create buckets of words that differ by one letter
#     for line in wfile:
#         word = line[:-1]
#         for i in range(len(word)):
#             bucket = word[:i] + '_' + word[i+1:]
#             if bucket in d:
#                 d[bucket].append(word)
#             else:
#                 d[bucket] = [word]
#     # add vertices and edges for words in the same bucket
#     for bucket in d.keys():
#         for word1 in d[bucket]:
#             for word2 in d[bucket]:
#                 if word1 != word2:
#                     g.addEdge(word1,word2)
#     return g



# from pythonds.graphs import Graph, Vertex
# from pythonds.basic import Queue
#
# def bfs(g,start):
#   start.setDistance(0)
#   start.setPred(None)
#   vertQueue = Queue()
#   vertQueue.enqueue(start)
#   while (vertQueue.size() > 0):
#     currentVert = vertQueue.dequeue()
#     for nbr in currentVert.getConnections():
#       if (nbr.getColor() == 'white'):
#         nbr.setColor('gray')
#         nbr.setDistance(currentVert.getDistance() + 1)
#         nbr.setPred(currentVert)
#         vertQueue.enqueue(nbr)
#     currentVert.setColor('black')



# def traverse(y):
#     x = y
#     while (x.getPred()):
#         print(x.getId())
#         x = x.getPred()
#     print(x.getId())
#
# traverse(g.getVertex('sage'))



# from pythonds.graphs import Graph
# class DFSGraph(Graph):
#     def __init__(self):
#         super().__init__()
#         self.time = 0
#
#     def dfs(self):
#         for aVertex in self:
#             aVertex.setColor('white')
#             aVertex.setPred(-1)
#         for aVertex in self:
#             if aVertex.getColor() == 'white':
#                 self.dfsvisit(aVertex)
#
#     def dfsvisit(self,startVertex):
#         startVertex.setColor('gray')
#         self.time += 1
#         startVertex.setDiscovery(self.time)
#         for nextVertex in startVertex.getConnections():
#             if nextVertex.getColor() == 'white':
#                 nextVertex.setPred(startVertex)
#                 self.dfsvisit(nextVertex)
#         startVertex.setColor('black')
#         self.time += 1
#         startVertex.setFinish(self.time)



