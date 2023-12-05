from collections import namedtuple
from math import ceil

with open('input9.txt', 'r') as f:
    moves = [line.strip().split(' ') for line in f.readlines()]

Point = namedtuple('Point', ['x', 'y'])

visited = {Point(0, 0)}
head, tail = Point(0, 0), Point(0, 0)
for move in moves:
    d = move[0]
    steps = int(move[1])
    while steps > 0:
        steps -= 1
        if d == 'U':
            head = Point(head.x, head.y+1)
        if d == 'R':
            head = Point(head.x+1, head.y)
        if d == 'D':
            head = Point(head.x, head.y-1)
        if d == 'L':
            head = Point(head.x-1, head.y)

        distance = (head.x - tail.x, head.y - tail.y)
        magnitude = Point(abs(distance[0]), abs(distance[1]))
        direction = Point(
            0 if distance[0] == 0 else distance[0] / magnitude[0],
            0 if distance[1] == 0 else distance[1] / magnitude[1]
        )

        if 2 in magnitude:
            tail = Point(
                tail.x + (direction.x * ceil(magnitude.x / 2)),
                tail.y + (direction.y * ceil(magnitude.y / 2))
            )

        visited.add(tail)

print(len(visited))  # 5513
