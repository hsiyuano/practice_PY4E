fname = input("Enter file name:")
fh = open(fname)
text = fh.read().strip()
print (text.upper())