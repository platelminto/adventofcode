import heapq
import json
import re
from dataclasses import dataclass
from functools import reduce
from queue import PriorityQueue
from typing import List, Callable


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[False for _ in range(num_of_vertices)] for _ in range(num_of_vertices)]
        self.visited = []


def dijkstra(graph, start_vertex):
    D = {v: float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor]:
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + 1
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


def get_neighbours(i, j, max_i, max_j):
    neighbours = []
    if i > 0:
        neighbours.append((i-1, j))
    if i < max_i-1:
        neighbours.append((i+1, j))
    if j > 0:
        neighbours.append((i, j-1))
    if j < max_j-1:
        neighbours.append((i, j+1))

    return neighbours


def main():
    with open('input12.txt', 'r') as f:
        heightmap = [line.strip() for line in f.readlines()]

    size = len(heightmap) * len(heightmap[0])

    g = Graph(size)

    start, end = -1, -1
    for i, line in enumerate(heightmap):
        for j, char in enumerate(line):
            v = i * len(line) + j
            if char == 'S':
                start = v
                heightmap[i] = heightmap[i][:j] + 'a' + heightmap[i][j+1:]
            if char == 'E':
                end = v
                heightmap[i] = heightmap[i][:j] + 'z' + heightmap[i][j + 1:]

    for i, line in enumerate(heightmap):
        for j, char in enumerate(line):
            vertex = i * len(line) + j
            for nbr_i, nbr_j in get_neighbours(i, j, len(heightmap), len(line)):
                nbr_vertex = nbr_i * len(line) + nbr_j
                if ord(heightmap[nbr_i][nbr_j]) - ord(char) <= 1:
                    g.edges[vertex][nbr_vertex] = True

    print(dijkstra(g, start)[end])


if __name__ == '__main__':
    main()  # 504
