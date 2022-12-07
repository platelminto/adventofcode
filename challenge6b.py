with open('input6a.txt', 'r') as f:
    text = f.read()

for i in range(len(text)):
    if len(set(text[i:i + 14])) == len(text[i:i + 14]):
        break

print(i+14)  # 3217
