import heapq
import json
import re
from dataclasses import dataclass
from functools import reduce
from typing import List, Callable


class Monkey:
    def __init__(self,
                 items: List[int],
                 operation: Callable[[int], int],
                 test: Callable[[int], int],
                 ):
        self.items = items
        self.operation = operation
        self.test = test


def get_monkeys():
    with open('input11.txt', 'r') as f:
        monkeys_text = f.read().split('\n\n')

    monkeys = []
    for monkey_text in monkeys_text:
        lines = monkey_text.strip().split('\n')

        starting_items = json.loads(f"[{lines[1].split(': ')[1]}]")

        def operation(old, lines=lines):
            return eval(lines[2].split('new = ')[1])

        def test(x, lines=lines):
            divisible_by = int(re.match(r'.*?(\d+)', lines[3]).group(1))
            if x % divisible_by == 0:
                return int(re.match(r'.*?(\d+)', lines[4]).group(1))
            else:
                return int(re.match(r'.*?(\d+)', lines[5]).group(1))

        monkeys.append(Monkey(starting_items, operation, test))

    return monkeys


def main():
    monkeys = get_monkeys()

    inspections = [0] * len(monkeys)

    for round in range(10000):
        for i, monkey in enumerate(monkeys):
            inspections[i] += len(monkey.items)
            while monkey.items:
                item = monkey.items.pop(0)
                item = monkey.operation(item)
                item %= 9699690
                monkeys[monkey.test(item)].items.append(item)

    print(reduce(lambda x, y: x * y, heapq.nlargest(2, inspections)))


if __name__ == '__main__':
    main()  # 21553910156
