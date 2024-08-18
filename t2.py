class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self,person,frind):
        if person not in self.graph:
            self.graph[person] = []
            self.graph[person].append(frind)

    def bfs(self,start,goal):
        visited = set()
        queue = [start]

        while queue:
            vertex = queue.pop(0)
            if vertex == goal:
                return 'True'
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(self.graph.get(vertex,[]))
        return 'False'


relationGraph = Graph()
n = int(input())
for _ in range(n):
    line = input()
    person, f = line.split('#')
    frinds_list = f.split('-')
    for frind in frinds_list:
        relationGraph.addEdge(person,frind)

start, goal = input().split('-')
result = relationGraph.bfs(start, goal)
print(result)
