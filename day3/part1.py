file_path = './input.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

sum = 0

for line in lines:
    value = line.strip()

    tens = (0, 0)
    unit = (0, 0)

    for i in range(0, len(value)):
        num = int(value[i])

        if num > tens[0] and i != len(value) - 1:
            tens = (num, i)
    
    for i in range(tens[1] + 1, len(value)):
        num = int(value[i])

        if num > unit[0]:
            unit = (num, i)

    sum += tens[0] * 10 + unit[0]

print(sum)