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
    move_n, from_col, to_col = int(move_n), int(from_col), int(to_col)

    state[to_col] = state[from_col][:move_n] + state[to_col]
    state[from_col] = state[from_col][move_n:]

print(''.join([col[0] for col in state[1:]]))
