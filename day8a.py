import copy

with open('input8.txt', 'r') as f:
    text = f.readlines()

original_forest = [[int(height) for height in list(line.strip())] for line in text]
is_visible = [[False for tree in trees] for trees in original_forest]

forest = copy.deepcopy(original_forest)
for row, trees in enumerate(forest):
    is_visible[row][0] = True
    for col in range(1, len(trees)):
        if trees[col-1] < trees[col]:
            is_visible[row][col] = True
        trees[col] = max(trees[col-1], trees[col])

forest = copy.deepcopy(original_forest)
for row, trees in enumerate(forest):
    n_trees = len(trees)
    is_visible[row][n_trees-1] = True
    for col in range(1, len(trees)+1):
        if trees[n_trees - col-1] < trees[col]:
            is_visible[row][col] = True
        trees[col] = max(trees[col-1], trees[col])

print(forest)  # never worked
