#Ex 11.2
import re

fname = input('Enter file name: ')
fhand = open(fname)
total = 0

for line in fhand:
    numbers = re.findall('[0-9]+', line)
    if not numbers:
        continue
    else:
        for number in numbers:
            total += float(number)

print(total)
