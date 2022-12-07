with open('input6.txt', 'r') as f:
    text = f.read()

for i in range(len(text)):
    if len(set(text[i:i + 4])) == len(text[i:i + 4]):
        break

print(i+4)  # 1175
