file_path = './input.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()
    lines = list(map(lambda e: e.strip(), lines))

ranges = []

for rangeStr in lines[:lines.index('')]:
    start, end = rangeStr.split('-')

    ranges.append((int(start), int(end) + 1))

ranges.sort()

sum = 0
cursor = 0

for start, end in ranges:
    if cursor >= end:
        continue

    sum += min(end - cursor, end - start)

    cursor = end

print(sum)