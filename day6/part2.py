import re
from functools import reduce
from typing import Callable

file_path = './input.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

operations = re.split(r'\s(?!\s|$)', lines[-1])

values = lines[:-1]
lengths = list(map(lambda x: len(x), operations))
result: list[list[str]] = []
for s in values:
    parts: list[str] = []
    i = 0

    for length in lengths:
        parts.append(s[i:i + length].replace('\n', ''))
        i += length + 1
        
    result.append(parts)

total = 0

for i, operator in enumerate(operations):
    op = operator.strip()

    length = len(operator)
    terms = list(map(lambda e: list(e[i]), result))

    transposed = [[terms[j][i] for j in range(len(terms))] for i in range(len(terms[0]))]

    terms = [int(''.join(t)) for t in transposed]
    
    start = 1 if op == '*' else 0
    fn: Callable[[int, int], int] = (lambda x, y: x * y) if op == '*' else (lambda x, y: x + y)

    total += reduce(fn, terms, start)

print(total)