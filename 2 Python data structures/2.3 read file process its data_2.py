fname = input("Enter file name:")
fh = open (fname)
tot = 0 # place outside the for loop
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):continue
    words = line.split()# split where the white space, tabs, newline character is

    tot = tot + float(words[1]) # float the 1st position in word string, place inside the for look, 
    count = count + 1 # take the current value of count, add 1, and save the new value back into count
print ("Average spam confidence:", tot/count)