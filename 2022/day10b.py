import re
from dataclasses import dataclass

with open('input10.txt', 'r') as f:
    commands = f.readlines()


@dataclass
class Memory:
    add: int
    cycles: int


def parse_command(command):
    if m := re.match("addx (-?\d+)", command):
        return Memory(int(m.group(1)), 2)

    return Memory(0, 1)


x = 1
cycle = 0
mem = parse_command(commands.pop(0))
crt = ""
while commands:
    if cycle % 40 == 0:
        crt += '\n'
    if x-1 <= cycle % 40 <= x+1:
        crt += "#"
    else:
        crt += '.'

    cycle += 1
    mem = Memory(mem.add, mem.cycles-1)

    if mem.cycles == 0:
        x += mem.add
        mem = parse_command(commands.pop(0))


print(crt)  # BPJAZGAP
