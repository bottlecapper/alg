
# visits all the nodes of a graph (connected component) using BFS
def bfs_connected_component(graph, start):
    # Store all visited nodes
    res = []
    # Keep track of nodes to be checked
    queue = [start]

    levels = {}         # Keeps track of levels of each node
    levels[start] = 0   # Depth of start node is 0

    visited = [start]   # Avoid inserting the same node twice into the queue

    # Keep looping while queue is not empty
    while queue:
       # Pop shallowest node (first node) from queue
        node = queue.pop(0)
        res.append(node)
        neighbours = graph[node]

        # Add neighbours of node to queue
        for vertex in neighbours:
            if vertex not in visited:
                queue.append(vertex)
                visited.append(vertex)

                levels[vertex]= levels[node]+1
                # print(vertex, ">>", levels[vertex])

    print(levels)
    return res


# sample graph implemented as a dictionary
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

ans = bfs_connected_component(graph,'A') # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']
print(ans)

