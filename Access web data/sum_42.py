fhand = open ("regex_sum_42.txt")
import re #improt regular expression
total = 0
for line in fhand:
    numbers = re.findall('[0-9]+',line)
    for number in numbers:
        total = total + int (number)
print (total)
