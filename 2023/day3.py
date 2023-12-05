import re
from collections import defaultdict


def get_surrounding(line_index: int, char_index: int, lines: list[str]) -> list[tuple[str, int, int]]:
    indexes = [(line_index + i, char_index + j) for i in (-1, 0, 1) for j in (-1, 0, 1)]

    return [(lines[i][j], i, j) for i, j in indexes if 0 <= i < len(lines) and 0 <= j < len(lines[line_index])]


def part1():
    with open("inputs/3.txt") as f:
        lines = f.readlines()

    # ugly, ugly code...
    parts_sum = 0
    for i, line in enumerate(lines):
        for m in re.finditer(r"(\d+)", line):
            # newlines fucked you up! since we're looking for chars that *don't* matter.
            if any(
                    any(not re.match(r"\.|\d|\n", c) for c, _, _ in get_surrounding(i, char_index, lines))
                    for char_index in range(m.start(1), m.end(1))
            ):
                parts_sum += int(m[1])

    print(parts_sum)


def part2():
    with open("inputs/3.txt") as f:
        lines = f.readlines()

    gear_adjacents = defaultdict(list)
    for i, line in enumerate(lines):
        for m in re.finditer(r"(\d+)", line):
            gear_indexes = set()
            for char_index in range(m.start(1), m.end(1)):
                for c, c_i, c_j in get_surrounding(i, char_index, lines):
                    if c == "*":
                        gear_indexes.add((c_i, c_j))

            for c_i, c_j in gear_indexes:
                gear_adjacents[(c_i, c_j)].append(int(m[1]))

    print(sum(ns[0] * ns[1] for ns in gear_adjacents.values() if len(ns) == 2))


if __name__ == "__main__":
    part1()
    part2()
