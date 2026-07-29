fhand = open("mbox-short.txt")

counts = dict ()

for line in fhand:
    line = line.rstrip()
    if not line.startswith ('From '): 
        continue
    words = line.split()
    sender = words[1]
    counts[sender] = counts.get(sender,0) + 1
        
bigcount = None
bigword = None

for sender, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = sender
        bigcount = count
print(bigword, bigcount)
