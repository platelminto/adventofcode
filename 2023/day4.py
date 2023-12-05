import re
from collections import defaultdict


def part1():
    points = 0
    with open("inputs/4.txt") as f:
        for line in f.readlines():
            _, winning_line, our_line = re.split(r"[:|]", line)
            winning_numbers = [int(x) for x in re.split(r"\s", winning_line) if x]
            our_numbers = [int(x) for x in our_line.split(" ") if x]

            matching = 0
            for our_n in our_numbers:
                if our_n in winning_numbers:
                    matching += 1

            points += 2 ** (matching-1) if matching else 0

    print(points)


def part2():
    with open("inputs/4.txt") as f:
        lines = f.readlines()

        copies = defaultdict(lambda: 1)
        for i, line in enumerate(lines):
            card_n = i + 1
            if card_n not in copies:
                copies[card_n] = 1

            _, winning_line, our_line = re.split(r"[:|]", line)
            winning_numbers = [int(x) for x in re.split(r"\s", winning_line) if x]
            our_numbers = [int(x) for x in our_line.split(" ") if x]

            matching = 0
            for our_n in our_numbers:
                if our_n in winning_numbers:
                    matching += 1

            for other_card_n in range(card_n + 1, card_n + matching + 1):
                copies[other_card_n] += copies[card_n]

    print(sum(copies.values()))


if __name__ == "__main__":
    part1()
    part2()
