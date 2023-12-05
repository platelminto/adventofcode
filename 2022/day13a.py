import heapq
import json
import re
from dataclasses import dataclass
from functools import reduce
from queue import PriorityQueue
from typing import List, Callable

T = list[int | list]


def right_order(og_left: list[int | T], og_right: list[int | T], left_i: int, right_i: int, parent, parent_i):
    if left_i == len(og_left) and right_i == len(og_right):
        return right_order(og_left)
    if left_i == len(og_left):
        return True
    if right_i == len(og_right):
        return False

    left, right = og_left[left_i], og_right[right_i]

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        if right < left:
            return False

        return right_order(og_left, og_right, left_i+1, right_i+1, parent, parent_i)

    if not (isinstance(left, list) and isinstance(right, list)):
        if isinstance(left, int):
            left = [left]
        else:
            right = [right]

    return right_order(left, right, 0, 0, parent, parent_i)


def main():
    with open('input13.txt', 'r') as f:
        pairs = f.read().split('\n\n')

    index_sum = []
    for i, pair in enumerate(pairs):
        i = i + 1
        print(i)

        left, right = pair.strip().split('\n')
        left = json.loads(left)
        right = json.loads(right)

        if right_order(left, right, 0, 0):
            index_sum.append(i)

    print(index_sum)


if __name__ == '__main__':
    main()  #
