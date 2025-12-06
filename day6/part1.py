import re
from functools import reduce
from typing import Callable

file_path = './input.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

operations = [re.split(r'\s+', s) for s in [lines[-1].strip()]][0]
values = [re.split(r'\s+', s.strip()) for s in lines[:-1]]

total = 0

print(values)

for i, op in enumerate(operations):
    terms = list(map(lambda e: int(e[i]), values))
    result = None
    start = 1 if op == '*' else 0
    fn: Callable[[int, int], int] = (lambda x, y: x * y) if op == '*' else (lambda x, y: x + y)

    result = reduce(fn, terms, start)

    total += result

print(total)