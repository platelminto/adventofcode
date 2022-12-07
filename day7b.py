import re
from dataclasses import dataclass
from typing import List


@dataclass
class File:
    size: int


class Directory:
    entries: dict

    def __init__(self, parent):
        self.parent = parent
        self.entries = {}

    def get_dir(self, name: str):
        if name == '..':
            return self.parent

        if name not in self.entries:
            self.entries[name] = Directory(self)

        return self.entries[name]

    @property
    def size(self) -> int:
        return sum([e.size for e in self.entries.values()])


def generate_filesystem(instructions_file) -> Directory:
    with open(instructions_file) as f:
        text = [line.strip() for line in f.readlines()[1:]]

    dir = Directory(None)
    for line in text:
        if m := re.match(r'^\$ cd (.+)$', line):
            cd_dir = m.group(1)
            dir = dir.get_dir(cd_dir)

        elif m := re.match(r'(\d+) (.+)', line):
            size, name = int(m.group(1)), m.group(2)
            dir.entries[name] = File(size)

    # Reset dir to root
    while dir.parent:
        dir = dir.parent

    return dir


def all_dirs(root_dir: Directory) -> List[Directory]:
    dirs = []
    for entry in root_dir.entries.values():
        if isinstance(entry, Directory):
            dirs.append(entry)
            dirs.extend(all_dirs(entry))

    return dirs


if __name__ == '__main__':
    root = generate_filesystem('input7.txt')

    min_size = root.size
    for d in all_dirs(root):
        if d.size >= root.size - 40_000_000:
            min_size = min(min_size, d.size)

    print(min_size)  # 2877389
