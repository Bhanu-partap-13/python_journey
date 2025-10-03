
class Graph:
    def __init__(self):
        self.graph = {}   # dictionary to store graph adjacency list

    # 1️⃣ Add a vertex to the graph
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            print(f"Vertex '{vertex}' added.")
        else:
            print(f"Vertex '{vertex}' already exists.")

    # 2️⃣ Add an edge between two vertices
    def add_edge(self, v1, v2):
        if v1 not in self.graph:
            self.add_vertex(v1)
        if v2 not in self.graph:
            self.add_vertex(v2)
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)   # for undirected graph
        print(f"Edge added between '{v1}' and '{v2}'.")

    # 3️⃣ Display the graph
    def display(self):
        print("\nGraph Adjacency List:")
        for vertex, neighbors in self.graph.items():
            print(f"{vertex} -> {', '.join(map(str, neighbors))}")

    # 4️⃣ Breadth First Search (BFS)
    def bfs(self, start):
        if start not in self.graph:
            print(f"Start vertex '{start}' not found!")
            return
        visited = set()
        queue = [start]
        print("\nBFS Traversal:", end=" ")
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        print()

    # 5️⃣ Depth First Search (DFS)
    def dfs(self, start):
        if start not in self.graph:
            print(f"Start vertex '{start}' not found!")
            return
        visited = set()
        print("\nDFS Traversal:", end=" ")
        self._dfs_helper(start, visited)
        print()

    def _dfs_helper(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited)


# 🧪 Example Usage
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')

g.display()

g.bfs('A')
g.dfs('A')
