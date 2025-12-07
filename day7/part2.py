from functools import cache

file_path = './input.txt'

with open(file_path, 'r') as file:
    lines = [l.strip() for l in file.readlines()]

total_timelines = 0

@cache
def compute_tl(i, j):
    if j + 1 < len(lines):
        char = lines[j + 1][i]

        if char == '.':
            return compute_tl(i, j + 1)
        
        if char == '^':
            return compute_tl(i + 1, j + 1) + compute_tl(i - 1, j + 1) + 1
        
    return 0

for j, line in enumerate(lines):
    for i, char in enumerate(line):
        if char == 'S':
            total_timelines = compute_tl(i, j) + 1

print(total_timelines)