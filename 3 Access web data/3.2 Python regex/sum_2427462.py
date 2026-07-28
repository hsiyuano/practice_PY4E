fhand = open ("regex_sum_2427462.txt")
import re
total = 0
for line in fhand:
    numbers = re.findall('[0-9]+',line)
    for number in numbers:
        total = total + int (number)
print (total)