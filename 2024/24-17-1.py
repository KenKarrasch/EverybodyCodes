f = open('24-17-2.txt').read().split('\n')

stars = []
print(f)
for x,ln in enumerate(f):
    y = 0
    for ch in ln:
        if ch == '*':
            stars.append((x,y))
        y += 1

print(stars)

def getdist(s1,s2):
    return(abs(s1[0] - s2[0]) + abs(s1[1] - s2[1]))


class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

def kruskal(graph):
    edges = [(weight, u, v) for u in graph for v, weight in graph[u].items()]
    edges.sort()
    vertices = list(graph.keys())
    disjoint_set = DisjointSet(vertices)
    minimum_spanning_tree = []

    for weight, u, v in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            minimum_spanning_tree.append((u, v, weight))

    return minimum_spanning_tree

graph = {}

for i in stars:
    gh = {}
    for j in stars:
        if i != j:
            #if getdist(i,j) < 6:
                gh[j] = getdist(i,j)
    graph[i] = gh

mst = kruskal(graph)
print("Minimum Spanning Tree:")
sm = []
for edge in mst:    
    print(f"{edge[0]} -- {edge[1]} : {edge[2]}")
    sm += {edge[2]}
print(sum(sm) + len(stars))
