with open("input3.txt") as f:
    text = f.readlines()

total = 0
for line in text:
    line = line.strip()
    left, right = line[:len(line)//2], line[len(line)//2:]
    extra = set(left).intersection(set(right)).pop()
    if extra.isupper():
        total += ord(extra) - 38
    else:
        total += ord(extra) - 96

print(total)