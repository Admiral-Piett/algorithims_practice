import random
import string

# from guppy import hpy
# h = hpy()
# print h.heap()

def generate_file(line_number, file_number=1):
    def generate_line():
        return ''.join([random.choice(string.ascii_letters) for i in range(0, 32)])


    saved_lines = []
    for i in range(0, file_number):
        i += 1
        f = open('strings_'+str(i)+'.txt', 'w+')

        for v in range(0, line_number):
            if i > 1 and len(saved_lines) > 0:
                if (v - 1) % 10 == 0:
                    line = saved_lines[0]
                    f.writelines(line + '\n')
                    saved_lines.pop(0)
                elif v == line_number-1:
                    f.writelines(generate_line())
                else:
                    f.writelines(generate_line()+'\n')
            else:
                if (v - 1)% 10 == 0:
                    line = generate_line()
                    f.writelines(line + '\n')
                    saved_lines.append(line)
                elif v == line_number-1:
                    f.writelines(generate_line())
                else:
                    f.writelines(generate_line()+'\n')

        f.close()

# generate_file(1000000, 2)
# print('finished generating files')

# python question2a.py strings_1.txt strings_2.txt  should run the analysis

import fileinput
checked = set()
count = 0

for line in fileinput.input():
    if fileinput.filename() == 'strings_1.txt':
        checked.add(line)
    else:
        if line in checked:
            count += 1

print(count)