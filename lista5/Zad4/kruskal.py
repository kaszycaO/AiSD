class SingleSet:
    def __init__(self, x):
        self.parent = self
        self.rank = 0
        self.value = x

def find(x):
    while x != x.parent:
        x = x.parent
    return x

def union(x,y):
    rootX = find(x)
    rootY = find(y)
    if rootX == rootY:
        return
    if rootX.rank > rootY.rank:
        rootY.parent = rootX
    else:
        rootX.parent = rootY
        if rootX.rank == rootY.rank:
            rootY.rank += 1

def makeset(n, G):
    graph = []
    sets = []
    for i in range(n):
        sets.append(SingleSet(i))

    for e in G:
        u = int(e[0])
        v = int(e[1])
        if u < v:
            graph.append((sets[u], sets[v], float(e[2])))
        else:
            graph.append((sets[v], sets[u], float(e[2])))

    return sorted(graph, key=lambda x: x[2])

def kruskal(n, G):
    new_graph = []
    edges = makeset(n, G)
    X = []
    for edge in edges:
        if find(edge[0]) != find(edge[1]):
            X.append(edge)
            union(edge[0], edge[1])
    return X
