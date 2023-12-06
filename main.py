import os

input_files = ['1.txt', '2.txt', '3.txt']
file_info = []

for file in input_files:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        file_info.append((file, len(lines)))

file_info.sort(key=lambda x: x[1])

output_file = 'result.txt'

with open(output_file, 'w', encoding='utf-8') as f:
    for file, num_lines in file_info:
        f.write(f'File: {file}\n')
        f.write(f'Number of lines: {num_lines}\n')
        with open(file, 'r', encoding='utf-8') as input_file:
            f.write(input_file.read())
        f.write('\n----------\n')

print(f'Файлы успешно объединены в {output_file}.')