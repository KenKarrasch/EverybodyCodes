f = open('24-17-3.txt').read().split('\n')

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

# Example usage
grph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

graph = {}

for i in stars:
    gh = {}
    for j in stars:
        if i != j:
            if getdist(i,j) < 6:
                gh[j] = getdist(i,j)
    graph[i] = gh

mst = kruskal(graph)
print("Minimum Spanning Tree:")
sm = []
for edge in mst:    
    print(f"{edge[0]} -- {edge[1]} : {edge[2]}")
    sm += {edge[2]}

distdb = []
print()

seen = set()
for star in stars:
    if star not in seen:
        sr = star    
        lseen = set()
        #print()
        #print(sr)
        Q = [(sr)]    
        dist = 0
        seen.add(sr)
        lseen.add(sr)
        while Q:          
            wl = Q.pop()     
            #print('pop',wl)         
            #print('seen',seen)
            for edge in mst:         
                #print('edge',edge)           
                if (edge[0] == wl) or (edge[1] == wl):                
                    if edge[1] not in seen:                    
                        dist += edge[2]                      
                        Q.append(edge[1])
                        #print('adding',edge[1])                   
                    if edge[0] not in seen:                  
                        dist += edge[2]                        
                        Q.append(edge[0])
                        #print('adding',edge[0])
                    seen.add(edge[0])
                    seen.add(edge[1])   
                    lseen.add(edge[0])
                    lseen.add(edge[1])                       
            #print('dist',dist)               
        distdb.append(dist + len(lseen))

            
print(distdb)
distdb.sort()
print(distdb[-3] * distdb[-2] * distdb[-1])

