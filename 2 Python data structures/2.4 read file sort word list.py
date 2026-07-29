fname = input("Enter file name:")
fh = open(fname)
lst = list() # create an empty lit

for line in fh: # read each line in file
    words = line.split() #split the line where white space is and assign to words, split() method returns a list of strings, so word is a string
    for word in words:# take ieach item from the list words, one at a time, and temporarily store in the valirable word
        if word in lst:
            continue #
        lst.append(word) # add one item at a time and change the original list, that is add the word in the variable lst

lst.sort()
print (lst)