import os
import re

input_folder = 'input'
output_folder = 'output'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
            block_lines = []
            for line in infile:
                if re.match(r'^\d{2}:\d{2}:\d{2}\n?$', line):
                    continue
                if re.match(r'^Speaker \d+: ', line):
                    line = re.sub(r'^Speaker \d+: ', '', line).strip()
                if line.strip() == '':
                    if block_lines:
                        outfile.write('\n'.join(block_lines) + '\n\n')
                        block_lines = []
                else:
                    line = re.sub(r'^\d{2}:\d{2}:\d{2}\nSpeaker \d+: ', '', line).strip()
                    block_lines.append(line)
            if block_lines:
                outfile.write('\n'.join(block_lines) + '\n')

