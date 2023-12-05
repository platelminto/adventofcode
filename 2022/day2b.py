shape_score = {
    'A': {
        'X': 3, 'Y': 1, 'Z': 2
    },
    'B': {
        'X': 1, 'Y': 2, 'Z': 3
    },
    'C': {
        'X': 2, 'Y': 3, 'Z': 1
    }
}

round_score = {
    'X': 0, 'Y': 3, 'Z': 6
}


with open('input2.txt', 'r') as f:
    matches = [line.strip().split(' ') for line in f.readlines()]

total_score = sum([shape_score[match[0]][match[1]] + round_score[match[1]] for match in matches])

print(total_score)