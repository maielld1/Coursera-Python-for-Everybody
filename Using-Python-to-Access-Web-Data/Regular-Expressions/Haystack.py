import re
handle = open('regex_sum_264795.txt')
numlist=list()
sum=0
for line in handle:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        sum=sum+int(number)
print sum
