import re

with open("input5.txt") as f:
    text = f.readlines()[10:]

inital_state = [
    '',
    'sphvfg',
    'mzdvbfjg',
    'njlmg',
    'pwdvzgn',
    'bcrv',
    'zlwpmsrv',
    'pht',
    'vzhcnsrq',
    'jqvpglf',
]

state = [list(x.upper()) for x in inital_state]

for instr in text:
    move_n, from_col, to_col = re.findall(r'\d+', instr)

    for _ in range(int(move_n)):
        state[int(to_col)].insert(0, state[int(from_col)].pop(0))

print(''.join([col[0] for col in state[1:]]))