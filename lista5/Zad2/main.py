#!/usr/bin/python3

import sys
from math import inf
from time import time

from priority_queue import PriorityQueue

def init_queue(data, length):
    queue = PriorityQueue()
    for i in range(length):
        queue.insert(i, data[i][0])

    return queue

def get_input():
    args = sys.stdin.readlines()
    args = [arg.split() for arg in args]

    try:
        args[0][0] = int(args[0][0])
        args[1][0] = int(args[1][0])
        args[2][0] = int(args[2][0])
    except ValueError:
        pass

    return args

def prepare_graph(args, V):
    G = [[] for _ in range(V)]
    for el in args:
        index = int(el[0])
        G[index].append((int(el[1]), float(el[2])))

    return G


def sigismund(G, s):
    """Dijkstra's Algoritm"""
    roads = [[inf, None] for _ in range(len(G))]
    roads[s][0] = 0
    roads[s][1] = s

    queue = init_queue(roads, len(G))

    while queue.length > 0:
        u = queue.pop()
        for edge in G[u]:
            if roads[edge[0]][0] > roads[u][0] + edge[1]:
                roads[edge[0]][0] = roads[u][0] + edge[1]
                roads[edge[0]][1] = u
                queue.priority(edge[0], roads[edge[0]][0])

    return roads



def interpret_results(dijkstra, s):
    result = []
    for i in range(len(dijkstra)):
        print(i, dijkstra[i][0])
        j = i
        route = []
        route.append(i)
        while j != s:
            helper = dijkstra[j][1]
            route.append(helper)
            j = helper
        route.reverse()
        result.append(route)

    return result

def print_route(roads, G):
    for new_road in roads:
        prev = new_road[0]
        sys.stderr.write(str(prev))
        if len(new_road) == 1:
            sys.stderr.write(": {} --> {}".format(0, prev))
            sys.stderr.write("\n")
            continue
        for el in new_road[1:]:
            j = 0
            while G[prev][j][0] != el:
                j += 1

            sys.stderr.write(": {} --> {}".format(G[prev][j][1], el))
            prev = el
        sys.stderr.write("\n")

def main():
    args = get_input()
    V = args[0][0]
    E = args[1][0]
    s = args[2][0]
    args = args[3:]
    if len(args) == E and s < V:
        clock = time()
        G = prepare_graph(args, V)
        dijkstra = sigismund(G, s)
        paths = interpret_results(dijkstra, s)
        print()
        print_route(paths, G)
        sys.stderr.write("Excecution time: {} ms".format((time()-clock)*1000))
        sys.stderr.write("\n")

    else:
        sys.stderr.write("Invalid input!")



if __name__ == "__main__":
    main()
