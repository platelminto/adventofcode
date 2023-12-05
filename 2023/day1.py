import re


def part1():
    total_sum = 0

    with open("inputs/1.txt") as f:
        for line in f.readlines():
            m = re.match(r".*?(\d).*(\d).*", line)
            if m:
                total_sum += int(m[1] + m[2])
            else:
                m = re.search(r"(\d)", line)
                total_sum += int(m[1] + m[1])

    print(total_sum)


digits = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

digits_regex = "|".join(list(digits.keys()) + list(digits.values()))

digits_translate = {k: k for k in digits.keys()}
digits_translate.update({v: k for k, v in digits.items()})


# Awful. Probably better to find all start indices of numbers (both digit and word-form), then use earliest & latest.
def part2():
    total_sum = 0

    with open("inputs/1.txt") as f:
        for line in f.readlines():
            m = re.match(rf".*?({digits_regex}).*({digits_regex}).*", line)
            if m:
                total_sum += int(digits_translate[m[1]] + digits_translate[m[2]])
            else:
                m = re.search(rf"({digits_regex})", line)
                total_sum += int(digits_translate[m[1]] + digits_translate[m[1]])

    print(total_sum)


if __name__ == "__main__":
    part1()
    part2()
