fname = open ("mbox-short.txt")

count = 0
for line in fname:
    line = line.rstrip() # remove white space from the right hand end (rstrip) of line, then save the cleaned string back into line
#python reads fine line by line
    if not line.startswith("From "):
        continue
    words = line.split()
    print (words[1])
    count = count + 1
print ("There were", count, "lines in the file with From as the first word")
