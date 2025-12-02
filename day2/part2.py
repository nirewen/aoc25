file_path = './input.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()
    line = lines[0].strip()

ranges = line.split(',')

sum = 0

for r in ranges:
    a, b = r.split('-')
    
    for num in range(int(a), int(b) + 1):
        numStr = str(num)

        repeatsList = []
        
        for i in range(1, len(numStr) + 1):
            if len(numStr) < i * 2:
                break

            part = numStr[:i]
            repeats = len(numStr) // i

            if numStr == part * repeats and not numStr in repeatsList:
                sum += num
                repeatsList.append(numStr)

print(sum)