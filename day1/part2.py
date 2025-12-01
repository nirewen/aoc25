file_path = './input.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

initial_value = 50

current_value = initial_value

zero_counter = 0

for line in lines:
    value = line.strip()
    
    direction = value[0]
    amount = int(value[1:])

    if direction == 'L':
        for i in range(0, amount):
            current_value -= 1

            if current_value < 0:
                current_value += 100

            if current_value == 0:
                zero_counter += 1

    if direction == 'R':
        for i in range(0, amount):
            current_value += 1

            if current_value > 99:
                current_value -= 100

            if current_value == 0:
                zero_counter += 1

print(zero_counter)