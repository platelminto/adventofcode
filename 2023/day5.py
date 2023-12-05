def part1():
    with open("inputs/5.txt") as f:
        text = f.read()

        sections = text.split("\n\n")

        seeds = [int(x) for x in sections[0].split(" ")[1:]]

        maps = []
        for section in sections[1:]:
            mappings = []
            for mapping in section.strip().split("\n")[1:]:
                mappings.append(tuple(int(x) for x in mapping.split(" ")))

            def map(number: int, mappings=mappings) -> int:
                for d_start, s_start, range_length in mappings:
                    if s_start <= number <= s_start + range_length:
                        return d_start + number - s_start

                return number

            maps.append(map)

        min_location = 10000000000000
        for seed in seeds:
            number = seed
            for map in maps:
                number = map(number)
            min_location = min(min_location, number)

        print(min_location)

def part2():
    with open("inputs/5.txt") as f:
        text = f.read()

        sections = text.split("\n\n")

        seeds = [int(x) for x in sections[0].split(" ")[1:]]

        seed_pairs = []
        for i, seed in enumerate(seeds[::2]):
            seed_pairs.append((seed, seeds[i+1]))

        maps = []
        for section in sections[1:]:
            mappings = []
            for mapping in section.strip().split("\n")[1:]:
                mappings.append(tuple(int(x) for x in mapping.split(" ")))

            maps.append(mappings)

        # go backwards from location
        maps = reversed(maps)

        for mappings in maps:
            mappings = sorted(mappings, key=lambda mapping: mapping[0])
            for mapping in mappings:
                pass


if __name__ == "__main__":
    part1()
    part2()
