from PIL import Image

file_path = './input.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

sum = 0

height = len(lines) - 1

grid = lines.copy()

frames = []

i = 0

def generate_animation(frames, output="animation.gif"):
    images = []
    width = len(frames[0])
    height = len(frames[0][0]) - 1

    for lines in frames:
        img = Image.new("RGB", (width, height), (0, 0, 0, 0))
        pixels = img.load()

        if pixels is None: break

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == '@':
                    pixels[x, y] = (255, 255, 255)

        images.append(img)
    
    images[0].save(
        output,
        save_all=True,
        append_images=images,
        duration=50,
        loop=0
    )

while True:
    removed = 0

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
                removed += 1

                a = list(grid[x])
                a[y] = '.'

                grid[x] = ''.join(a)

    frames.append(lines)

    i += 1

    if removed == 0:
        break

    sum += removed

    lines = grid.copy()

print(sum)

generate_animation(frames)