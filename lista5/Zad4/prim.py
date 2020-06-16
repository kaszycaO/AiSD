from math import inf
from priority_queue import PriorityQueue

def prepare_graph(args, V):
    G = [[] for _ in range(V)]
    done = [[False for _ in range(V)] for _ in range(V)]
    for el in args:
        u = int(el[0])
        v = int(el[1])
        if not (done[u][v] or done[v][u]):
            G[u].append((v, float(el[2])))
            G[v].append((u, float(el[2])))
        done[u][v] = True
    return G

def prim(n, input, s):
    G = prepare_graph(input, n)
    V = [[inf, None] for _ in range(n)]
    # s = randint(0, n-1)
    V[s][0] = 0
    V[s][1] = s
    Q = PriorityQueue()

    for i in range(n):
        Q.insert(i, V[i][0])

    visited = [False for _ in range(n)]
    while Q.length > 0:
        v = Q.pop()
        for edge in G[v]:
            z = edge[0]
            if V[z][0] > edge[1] and not visited[z]:
                V[z][0] = edge[1]
                V[z][1] = v
                Q.priority(z, edge[1])
                visited[z] = True
    return V
