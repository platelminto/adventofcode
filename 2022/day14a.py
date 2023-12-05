def main():
    with open('input14.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    rocks = set()
    max_y = 0
    for line in lines:
        points = line.split(' -> ')

        for i, point in enumerate(points[:-1]):
            next_point = points[i+1]
            p_x, p_y = point.split(',')
            n_x, n_y = next_point.split(',')

            p_x, p_y, n_x, n_y = int(p_x), int(p_y), int(n_x), int(n_y)

            x_step = 1 if n_x > p_x else -1
            y_step = 1 if n_y > p_y else -1

            for x in range(p_x, n_x + x_step, x_step):
                for y in range(p_y, n_y + y_step, y_step):
                    rocks.add((x, y))
                    max_y = max(max_y, y)

    added_rocks = 0
    curr_x, curr_y = 500, 0
    while curr_y <= max_y:
        if (curr_x, curr_y + 1) not in rocks:
            curr_y += 1
            continue
        if (curr_x - 1, curr_y + 1) not in rocks:
            curr_y += 1
            curr_x -= 1
            continue
        if (curr_x + 1, curr_y + 1) not in rocks:
            curr_y += 1
            curr_x += 1
            continue

        added_rocks += 1
        rocks.add((curr_x, curr_y))
        curr_x, curr_y = 500, 0


    print(added_rocks)

if __name__ == '__main__':
    main()  # 808
