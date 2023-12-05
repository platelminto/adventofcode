with open("input4.txt") as f:
    text = f.readlines()

total = 0
for line in text:
    line = line.strip()
    left, right = line.split(',')
    left = (int(left.split('-')[0]), int(left.split('-')[1]))
    right = (int(right.split('-')[0]), int(right.split('-')[1]))
    if left[1] - left[0] > right[1] - right[0]:
        left, right = right, left

    if left[0] >= right[0] and left[1] <= right[1]:
        total += 1

print(total)