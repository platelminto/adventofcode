with open('input8.txt', 'r') as f:
    text = f.readlines()

forest = [[int(height) for height in list(line.strip())] for line in text]

visible = 0
for row, trees in enumerate(forest):
    for col, height in enumerate(trees):
        column_trees = [forest[i][col] for i in range(len(trees))]

        if all([h < height for h in trees[:col]]) or all([h < height for h in trees[col + 1:]]) or \
                all([h < height for h in column_trees[:row]]) or all([h < height for h in column_trees[row + 1:]]):
            visible += 1

print(visible)  # 1832

