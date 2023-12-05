with open('input6.txt', 'r') as f:
    text = f.read()

for i in range(len(text)):
    header = text[i:i + 4]
    if len(set(header)) == len(header):
        break

print(i+4)  # 1175
