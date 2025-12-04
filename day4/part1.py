file_path = './input.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

sum = 0

height = len(lines) - 1

for x, line in enumerate(lines):
    value = line.strip()
    width = len(value)

    for y, char in enumerate(value):
        if char != '@': continue

        adjacent = [
            # top row
            lines[x - 1][y - 1] if x > 0 and y > 0     else None,
            lines[x - 1][y]     if x > 0               else None,
            lines[x - 1][y + 1] if x > 0 and y < width else None,

            # middle
            lines[x][y - 1] if y > 0     else None,
            lines[x][y + 1] if y < width else None,

            # bottom row
            lines[x + 1][y - 1] if x < height and y > 0     else None,
            lines[x + 1][y]     if x < height               else None,
            lines[x + 1][y + 1] if x < height and y < width else None
        ]

        adjacent = list(filter(lambda i:
            i == '@'                  
        , adjacent))

        if len(adjacent) < 4:
            sum += 1

print(sum)