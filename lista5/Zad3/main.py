#!/usr/bin/python3
import sys
from random import randint
from math import inf

from priority_queue import PriorityQueue

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

def prim(n, input):
    G = prepare_graph(input, n)
    V = [[inf, None] for _ in range(n)]
    s = randint(0, n-1)
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

def main():
    if len(sys.argv) == 2:
        option = sys.argv[1]

        args = sys.stdin.readlines()
        args = [arg.split() for arg in args]

        n = int(args[0][0])
        m = int(args[1][0])
        args = args[2:]

        if len(args) == m:
            if option == '-k':
                res = kruskal(n, args)
                total = 0
                for el in res:
                    print(el[0].value, el[1].value, el[2])
                    total += el[2]
                print(total)

            elif option == '-p':
                res = prim(n, args)
                total = 0
                for i in range(len(res)):
                    if i < res[i][1]:
                        print(i, res[i][1], res[i][0])
                    else:
                        print(res[i][1], i, res[i][0])
                    total += res[i][0]
                print(total)

            else:
                sys.stderr.write("Invalid parameter: \n", option)

        else:
            sys.stderr.write("Invalid input!\n")
    else:
        sys.stderr.write("Invalid number of parameters! Use just -p or -k\n")







if __name__ == "__main__":
    main()
