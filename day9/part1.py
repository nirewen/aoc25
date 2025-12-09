file_path = './input.txt'

with open(file_path, 'r') as file:
    lines = [l.strip() for l in file.readlines()]

points = [eval(s) for s in lines]

largest_area = 0

for p1 in points:
    for p2 in points:
        w = abs(p1[0] - p2[0]) + 1
        h = abs(p1[1] - p2[1]) + 1

        area = w * h

        if area > largest_area:
            largest_area = area

print(largest_area)