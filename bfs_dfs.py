"""
File Name: graph.py

Purpose:
--------
This file contains the implementation of a Graph using
Adjacency List representation.

Traversals implemented:
- Breadth First Search (BFS)
- Depth First Search (DFS)

Graphs are used to represent networks such as
social networks, maps, and computer networks.

Time Complexity:
----------------
BFS: O(V + E)
DFS: O(V + E)

Space Complexity:
-----------------
O(V + E)
"""

from collections import deque


class Graph:
    def __init__(self):
        # Dictionary to store adjacency list
        self.graph = {}

    def add_edge(self, u, v):
        # Add edge u -> v
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

        # For undirected graph, uncomment below
        # if v not in self.graph:
        #     self.graph[v] = []
        # self.graph[v].append(u)

    def bfs(self, start):
        # Set to keep track of visited nodes
        visited = set()

        # Queue for BFS
        queue = deque([start])
        visited.add(start)

        print("BFS Traversal:", end=" ")

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def dfs(self, start):
        # Set to track visited nodes
        visited = set()
        print("DFS Traversal:", end=" ")
        self._dfs_util(start, visited)

    def _dfs_util(self, node, visited):
        # Mark node as visited
        visited.add(node)
        print(node, end=" ")

        for neighbor in self.graph.get(node, []):
            if neighbor not in visited:
                self._dfs_util(neighbor, visited)


# ------------------ Example Usage ------------------

g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

g.bfs(0)
print()
g.dfs(0)
