import sys
from time import time
from random import randint
from random import seed
from math import inf
import tracemalloc

from prim import prim
from kruskal import kruskal
from priority_queue import PriorityQueue


def get_input():
    args = sys.stdin.readlines()
    args = [arg.split() for arg in args]

    try:
        args[0][0] = int(args[0][0])
        for i in range(1, len(args)):
            args[i][0] = int(args[i][0])
            args[i][1] = int(args[i][1])
            args[i][2] = float(args[i][2])
    except ValueError:
        print("Error!")

    return args

def prepare_graph(n, args):
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for el in args:
        graph[el[0]][el[1]] = el[2]
        graph[el[1]][el[0]] = el[2]
    return graph

def check_if_correct(route, n):
    for i in range(n):
        if i not in route:
            return False

    return True

def shortest_walk(n, s, G):
    tracemalloc.start()
    visited = [False for _ in range(n)]
    visited[s] = True

    route = []
    route.append(s)

    cost = 0
    curr = s
    while False in visited:
        dest = -1
        m = inf
        for i in range(n):
            if not visited[i] and G[curr][i] < m and i != curr:
                dest = i
                m = G[curr][i]
        visited[dest] = True
        cost += m
        curr = dest
        route.append(curr)

    memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    return cost, memory, route, len(route)

def random_walk(n, s, G):
    tracemalloc.start()

    visited = [False for _ in range(n)]
    visited[s] = True

    route = []
    route.append(s)

    cost = 0
    steps = 0
    curr = s
    while False in visited:
        dest = randint(0, n-1)
        if not visited[dest] and G[curr][dest] != 0:
            cost += G[curr][dest]
            curr = dest
            route.append(curr)
            visited[curr] = True
        else:
            route.append(dest)
            cost += G[curr][dest]
            curr = dest

        steps += 1

    memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    return cost, memory, route, steps

def eulerKruskal(n, s, G, input):
    tracemalloc.start()
    cost = 0
    k = 0
    v = s
    MST = [[] for _ in range(n)]
    T = kruskal(n, input)
    for t in T:
        MST[t[0].value].append([t[1].value, 0])
        MST[t[1].value].append([t[0].value, 0])

    to_visit = len(T) * 2
    vertices = []
    while to_visit > 0:
        vertices.append(v)
        u = -1
        vi = 3
        for edg in MST[v]:
            if edg[1] < 2 and edg[1] < vi:
                u = edg[0]
                vi = edg[1]
        idx = MST[v].index([u, vi])
        MST[v][idx][1] += 1
        idx = MST[u].index([v, vi])
        MST[u][idx][1] += 1
        v = u
        to_visit -= 1

    visited = [False for _ in range(n)]
    i = 0
    route = []
    route.append(s)
    while i < len(vertices):
        if visited[vertices[i]]:
            vertices.pop(i)
        else:
            visited[vertices[i]] = True
            i += 1
    for i in range(0, n-1):
        k += 1
        cost += G[vertices[i]][vertices[i+1]]
        route.append(vertices[i+1])


    memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return cost, memory, route, len(route)

def eulerPrim(n, s, G, input):
    tracemalloc.start()
    cost = 0
    k = 0
    v = s
    MST = [[] for _ in range(n)]
    T = prim(n, input, s)

    for i in range(len(T)):
        MST[i].append([T[i][1], 0])
        MST[T[i][1]].append([i, 0])


    to_visit = len(T) * 2
    vertices = []
    while to_visit > 0:
        vertices.append(v)
        u = -1
        vi = 3
        for edg in MST[v]:
            if edg[1] < 2 and edg[1] < vi:
                u = edg[0]
                vi = edg[1]
        idx = MST[v].index([u, vi])
        MST[v][idx][1] += 1
        idx = MST[u].index([v, vi])
        MST[u][idx][1] += 1
        v = u
        to_visit -= 1


    visited = [False for _ in range(n)]
    route = []
    prev = vertices[0]
    for el in vertices[1:]:
        if visited[el]:
            vertices.remove(el)
        else:
            visited[el] = True
            cost += G[prev][el]
            route.append(el)
        prev = el



    memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return cost, memory, route, len(route)


def main():
    # tests = ["--rand", "--short", "--eulerK", "--eulerP"]
    if len(sys.argv) == 2:
        algoritm = sys.argv[1]
        args = get_input()
        n = args[0][0]
        m = (n*(n-1))/2
        args = args[1:]

        if len(args) == m:
            s = randint(0, n-1)
            start = time()
            G = prepare_graph(n, args)
            if algoritm == "--rand":
                cost, memory, route, steps = random_walk(n, s, G)
            elif algoritm == "--short":
                cost, memory, route, steps = shortest_walk(n, s, G)
            elif algoritm == "--eulerK":
                cost, memory, route, steps = eulerKruskal(n, s, G, args)
            elif algoritm == "--eulerP":
                cost, memory, route, steps = eulerPrim(n, s, G, args)
            else:
                sys.stderr.write("Not correct algoritm!\n")
                return
            clock = time() - start

            sys.stderr.write("k        W              M[B]          t[ms]\n")
            sys.stderr.write("\n")
            print(steps, " ", cost, " ", memory, " ", clock*1000)

            for el in route:
                sys.stderr.write("{} ".format(str(el)))
            sys.stderr.write("\n")

        else:
            sys.stderr.write("Invalid input!")
    else:
        sys.stderr.write("Choose algoritm! --rand , --short, --eulerK, --eulerP\n")

if __name__ == "__main__":
    main()
