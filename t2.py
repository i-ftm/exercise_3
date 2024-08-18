class graph():
    def __init__(self):
        self.graph = {}

    def addEdge(self,person,frind):
        if person not in self.graph:
            self.graph['person'] = []
        self.graph['person'].append(frind)

    def bfs(self,start,goal):
        visited = set()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            visited.add(vertex)
            if vertex == goal:
                return 'True'
            queue.extend(self.graph.get(vertex,[]))
        return 'False'



g = graph()
n = int(input())
for _ in range(n):
    line = input()
    person , frinds = line.split('#')
    frinds_list = frinds.split('-')
    for frind in frinds_list:
        g.addEdge(person,frind)

start , goal = input().split('-')
result = g.bfs(start,goal)
print(result)