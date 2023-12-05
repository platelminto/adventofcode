import re


def get_cube_number(line: str, colour: str) -> int:
    search = re.search(rf"(\d+) {colour}", line)
    if search:
        return int(search[1])

    return 0


def part1(max_red: int, max_green: int, max_blue: int):
    ids_sum = 0
    with open("inputs/2.txt") as f:
        for line in f.readlines():
            id_part, sets = line.split(":")

            game_id = int(re.match(r".*?(\d+)$", id_part)[1])

            sets = sets.split(";")
            valid_game = True
            for cube_set in sets:
                if not all([
                    get_cube_number(cube_set, "red") <= max_red,
                    get_cube_number(cube_set, "green") <= max_green,
                    get_cube_number(cube_set, "blue") <= max_blue,
                ]):
                    valid_game = False

            if valid_game:
                ids_sum += game_id

    print(ids_sum)


def part2():
    sets_power_sum = 0
    with open("inputs/2.txt") as f:
        for line in f.readlines():
            _, sets = line.split(":")

            sets = sets.split(";")
            min_red, min_green, min_blue = 0, 0, 0
            for cube_set in sets:
                min_red = max(min_red, get_cube_number(cube_set, "red"))
                min_green = max(min_green, get_cube_number(cube_set, "green"))
                min_blue = max(min_blue, get_cube_number(cube_set, "blue"))

            sets_power_sum += min_red * min_green * min_blue

    print(sets_power_sum)


if __name__ == "__main__":
    part1(12, 13, 14)
    part2()
