shape_score = {
    'Y': 2,
    'X': 1,
    'Z': 3,
}

round_score = {
    'B': {
        'X': 0, 'Y': 3, 'Z': 6
    },
    'A': {
        'X': 3, 'Y': 6, 'Z': 0
    },
    'C': {
        'X': 6, 'Y': 0, 'Z': 3
    },
}


with open('input2a.txt', 'r') as f:
    matches = [line.strip().split(' ') for line in f.readlines()]

total_score = sum([shape_score[match[1]] + round_score[match[0]][match[1]] for match in matches])

print(total_score)