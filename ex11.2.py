#Ex 11.2
import re

rev = []

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be found')
    exit()

for line in fhand:
    line = line.rstrip()
    revision = re.findall('^New Revision: ([0-9.]+)', line)
    for x in revision:
        rev.append(float(x))


rev_sum = sum(rev)
count = float(len(rev))
rev_ave = int(rev_sum / count)

print(fname, ':', rev_ave)
