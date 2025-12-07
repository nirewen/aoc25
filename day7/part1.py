file_path = './input.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

tachyon_indexes = set()

splitted = 0

for i, line in enumerate(lines):
    line = line.strip()

    if i == 0:
        tachyon_indexes.add(line.find('S'))
        continue

    for j, char in enumerate(line):
        if char != '^': continue

        if j in tachyon_indexes:
            splitted += 1
            tachyon_indexes.update([j - 1, j + 1])
            tachyon_indexes.remove(j)

print(splitted)