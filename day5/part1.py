file_path = './input.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()
    lines = list(map(lambda e: e.strip(), lines))

ranges = lines[:lines.index('')]
ingredients = lines[lines.index('') + 1:]

spoiled_ingredients = set()

for ingredient in ingredients:
    for rangeStr in ranges:
        start, end = rangeStr.split('-')

        if int(ingredient) in range(int(start), int(end) + 1):
            spoiled_ingredients.add(ingredient)

print(len(spoiled_ingredients))