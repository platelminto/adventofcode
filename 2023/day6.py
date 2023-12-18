import math
import re


def get_solutions(a, b, c):
    d = math.sqrt(b ** 2 - 4 * a * c)

    sol1 = (-b + d) / (2 * a)
    sol2 = (-b - d) / (2 * a)

    return sol1, sol2


def part1(filenum="6"):
    with open(f"../2023/inputs/{filenum}.txt", "r") as f:
        data = f.read().split("\n")

    races = list(zip(re.split(r"\s+", data[0]), re.split(r"\s+", data[1])))[1:]

    beat = 1
    for r_time, r_distance in races:
        a = 1
        b = -int(r_time)
        c = int(r_distance)

        sol1, sol2 = get_solutions(a, b, c)

        # to always go up by 1.
        beat *= math.floor(sol1 - 0.0000001) - math.ceil(sol2 + 0.000001) + 1

    print(beat)


if __name__ == "__main__":
    part1()
    part1("6b")