file_path = './input.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

sum = 0

for line in lines:
    value = line.strip()

    final_num = ''

    for i in range(11, -1, -1):
        largest_value = 0
        largest_num = ''

        for j, numStr in enumerate(value):
            idx = len(value) - j - 1
            num = int(numStr) * 10 ** min(idx, i)

            if num >= largest_value:
                largest_num = numStr
                largest_value = num

        final_num += largest_num
        value = value[value.find(largest_num) + 1:]
    
    sum += int(final_num)

print(sum)