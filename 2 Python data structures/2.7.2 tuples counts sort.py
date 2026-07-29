name = input ("Enter files:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict() # create a dictionary
for line in handle: # read each line in the file
    wds = line.split() # split the line into word and store it into a list called wds
    if len(wds) < 5: # if the lengh of list less than 5
        continue
    if wds[0] != "From" : # if the 0 position of the list wds is From
        continue
    when = wds[5] # new string variable when assign to the 5th position of the list wds
    tics = when.split(":") # split the strings stored in when where finds a :, then store those part in list tics
    if len(tics) != 3:# if the length of the tics = 3
        continue
    hour = tics [0] # hour position is at the 0 position in list tics, assign it to string hour
    counts[hour] = counts.get(hour,0) + 1 # get the current count of how many times hour(as a key) value shown in dictionary count
lst = list(counts.items()) # counts.items() is the dictionary's key-value pairs, after conversion, each item in lst is a tuple
lst.sort()
for key, val in lst:
    print (key, val)