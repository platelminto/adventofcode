with open("input4.txt") as f:
    text = f.readlines()

total = 0
for line in text:
    line = line.strip()
    left, right = line.split(',')
    left = (int(left.split('-')[0]), int(left.split('-')[1]))
    right = (int(right.split('-')[0]), int(right.split('-')[1]))

    if right[0] <= left[0] <= right[1] or right[0] <= left[1] <= right[1] or \
        left[0] <= right[0] <= left[1] or left[0] <= right[1] <= left[1]:
        total += 1

print(total)
