with open('input8.txt', 'r') as f:
    text = f.readlines()

forest = [[int(height) for height in list(line.strip())] for line in text]

max_score = 1
for row, trees in enumerate(forest):
    for col, height in enumerate(trees):
        column_trees = [forest[i][col] for i in range(len(trees))]

        score = 1
        c = col-1
        for c in range(col-1, -1, -1):
            if trees[c] >= height:
                break
        score *= col - c
        c = col+1
        for c in range(col+1, len(trees)):
            if trees[c] >= height:
                break
        score *= c - col

        r = row-1
        for r in range(row-1, -1, -1):
            if column_trees[r] >= height:
                break
        score *= row - r
        r = row+1
        for r in range(row+1, len(column_trees)):
            if column_trees[r] >= height:
                break
        score *= r - row

        max_score = max(max_score, score)

print(max_score)  # 157320
