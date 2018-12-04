
"""
dfs
"""

# Use a stack to keep track of visited nodes, the last node seen is the next one to be visited, and the rest are stored
# to be visited later

# Algorithm - Pseudocode
# Initialize an empty stack for storage of nodes, S=[].
# For each vertex u, define u.visited to be False.
# Push the root (first node to be visited) into S.
# While S is not empty:
#     Pop the first element in S, u=S.pop().
#     If u.visited == False, then:
#         u.visited = True
#         for each unvisited neighbor w of u:       # neighbor defined in graph adjecent matrix
#             Push w into S.
# End process when all nodes have been visited.


class Solution:
    def dfs_visit(self, graph, root):
        visited = set()
        stack = [root]
        while stack:
            u = stack.pop()
            if u not in visited:
                visited.add(u)
                stack.extend(set(graph[u]) - visited)
        return visited


    def dfs_visit_recursive(self, graph, root, visited=set()):
        visited.add(root)
        for subroot in set(graph[root]) - visited:
            self.dfs_visit_recursive(graph, subroot)
        return visited


dfs = Solution()

adjacency_matrix = {1: [2, 7, 8],
                    2: [3, 6],
                    3: [4, 5],
                    4: [],
                    5: [],
                    6: [],
                    7: [],
                    8: [9, 12],
                    9: [10, 11],
                    10: [],
                    11: [],
                    12: []}

print(dfs.dfs_visit(adjacency_matrix, 1))
print(dfs.dfs_visit_recursive(adjacency_matrix, 1))
