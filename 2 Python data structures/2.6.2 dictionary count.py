name = input("Enter file:")
if len (name) < 1:
    name = "mbox-short.txt"
handle = open(name) #this should not be under if indentation

counts = dict()
for line in handle:# read each line of handle(that is file)
    wds = line.split() #split each line into list of words, place in variable wds
    if len(wds) < 2:
        continue
    if wds[0] != "From":
        continue
    email = wds[1] # assign the 1st position of wds list to email
    counts[email] = counts.get(email,0) + 1 # get() disctionary method, retrieve value connected to a key, 0 means it is not yet in the dictionary
    # counts[] in squeare brackaet because it is a dictionary

bigcount = None
bigname = None

for name, count in counts.items():
    if bigname is None or count > bigcount:
        bigname = name
        bigcount = count

print (bigname, bigcount)