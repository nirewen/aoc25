file_path = './input.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()
    line = lines[0].strip()

ranges = line.split(',')

sum = 0

for r in ranges:
    a, b = r.split('-')
    
    for num in range(int(a), int(b)):
        numStr = str(num)
        left, right = numStr[:len(numStr)//2], numStr[len(numStr)//2:]

        if numStr == f'{left}{left}':
            sum += num

print(sum)