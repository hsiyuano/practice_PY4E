fhand = open("mbox-short.txt")
counts = dict()

for line in fhand:
    line = line.rstrip()
    if not line.startswith ('From '): 
        continue
    words = line.split()
    time = words [5]
    
    pieces = time.split(':')
    hour = pieces [0]
    
    counts[hour] = counts.get(hour, 0) + 1

for hour, count in sorted(counts.items()):
    print (hour, count)
    
