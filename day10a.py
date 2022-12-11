import re
from dataclasses import dataclass

with open('input10.txt', 'r') as f:
    commands = f.readlines()
    commands += "noop"


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
signal_strength_sums = 0
mem = parse_command(commands.pop(0))
while cycle <= 220 and commands:
    cycle += 1
    mem = Memory(mem.add, mem.cycles-1)

    if cycle in [20, 60, 100, 140, 180, 220]:
        signal_strength_sums += cycle * x

    if mem.cycles == 0:
        x += mem.add
        mem = parse_command(commands.pop(0))

print(signal_strength_sums)  # 15140
