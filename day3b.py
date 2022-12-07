with open("input3.txt") as f:
    text = f.readlines()

chunks = [text[i:i+3] for i in range(0, len(text), 3)]

total = 0
for chunk in chunks:
    chunk = [line.strip() for line in chunk]
    common = set(chunk[0]).intersection(set(chunk[1])).intersection(set(chunk[2])).pop()

    if common.isupper():
        total += ord(common) - 38
    else:
        total += ord(common) - 96

print(total)